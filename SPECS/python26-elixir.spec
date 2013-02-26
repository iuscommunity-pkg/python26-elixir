%define __python /usr/bin/python2.6
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define pybase_ver 26
%define real_name python-elixir
%define name python%{pybase_ver}-elixir

Name:           %{name}
Version:        0.6.1
Release:        1.ius%{?dist}
Summary:        A declarative mapper for SQLAlchemy

Group:          Development/Languages
License:        MIT
URL:            http://elixir.ematia.de/
Source0:        http://cheeseshop.python.org/packages/source/E/Elixir/Elixir-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python%{pybase_ver}-devel, python%{pybase_ver}-setuptools

Requires:       python%{pybase_ver}-sqlalchemy


%description
Elixir is a declarative layer on top of SQLAlchemy. It is a fairly thin
wrapper, which provides the ability to define model objects following the
Active Record design pattern, and using a DSL syntax similar to that of the
Ruby on Rails ActiveRecord system.

Elixir does not intend to replace SQLAlchemy's core features, but instead
focuses on providing a simpler syntax for defining model objects when you do
not need the full expressiveness of SQLAlchemy's manual mapper definitions.


%prep
%setup -q -n Elixir-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
rm -rf build/lib/{tests,examples}/
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README TODO
# For noarch packages: sitelib
%{python_sitelib}/*


%changelog
* Mon Aug 25 2009 BJ Dierkes <wdierkes@rackspace.com> - 0.6.1-1.ius
- Rebuilding for IUS
- Latest sources from upstream

* Thu Dec 13 2007 James Bowes <jbowes@redhat.com> - 0.5.0-1
- Update to 0.5.0

* Wed Nov 14 2007 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.4.0-1
- Updated for upstream 0.4.0.

* Sun Jun 24 2007 James Bowes <jbowes@redhat.com> - 0.3.0-1
- Initial packaging for Fedora.
