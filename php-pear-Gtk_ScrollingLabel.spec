%define		_class		Gtk
%define		_subclass	ScrollingLabel
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(PHPUnit.php)

Name:		php-pear-%{upstream_name}
Version:	1.0.0
Release:	%mkrel 15
Summary:	A scrolling label for PHP-Gtk
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Gtk_ScrollingLabel/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a class to encapsulate the functionality needed for a
scrolling GTK+ label. This class provides a simple, easy to understand
API for setting up and controlling the label. It allows for the
ability to scroll in either direction, start and stop the scroll,
pause and unpause the scroll, get and set the text, and set display
properties of the text.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/example.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
