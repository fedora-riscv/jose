Name:           jose
Version:        3
Release:        1%{?dist}
Summary:        Tools for JSON Object Signing and Encryption (JOSE)

License:        ASL 2.0
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig
BuildRequires:  jansson-devel >= 2.9
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
José is a command line utility for performing various tasks on JSON
Object Signing and Encryption (JOSE) objects. José provides a full
crypto stack including key generation, signing and encryption.

%package -n lib%{name}
Summary:    Library implementing JSON Object Signing and Encryption

%description -n lib%{name}
This package contains a C library for performing JOSE operations.

%package -n lib%{name}-devel
Summary:        Development files for lib%{name}
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       jansson-devel

%description -n lib%{name}-devel
This package contains development files for lib%{name}.

%package -n lib%{name}-openssl
Summary:        Integration with OpenSSL for lib%{name}

%description -n lib%{name}-openssl
This package contains OpenSSL integration for lib%{name}.

%package -n lib%{name}-openssl-devel
Summary:        Development files for lib%{name}-openssl
Requires:       lib%{name}-openssl%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       openssl-devel

%description -n lib%{name}-openssl-devel
This package contains development files for lib%{name}-openssl.

%package -n lib%{name}-zlib
Summary:        Integration with zlib for lib%{name}

%description -n lib%{name}-zlib
This package contains zlib integration for lib%{name}.

%package -n lib%{name}-zlib-devel
Summary:        Development files for lib%{name}-zlib
Requires:       lib%{name}-zlib%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description -n lib%{name}-zlib-devel
This package contains development files for lib%{name}-zlib.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/%{_libdir}/lib%{name}.la
rm -rf %{buildroot}/%{_libdir}/lib%{name}-openssl.la
rm -rf %{buildroot}/%{_libdir}/lib%{name}-zlib.la

%check
make %{?_smp_mflags} check

%post -n lib%{name} -p /sbin/ldconfig
%post -n lib%{name}-zlib -p /sbin/ldconfig
%post -n lib%{name}-openssl -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name}-zlib -p /sbin/ldconfig
%postun -n lib%{name}-openssl -p /sbin/ldconfig

%files
%{_bindir}/%{name}

%files -n lib%{name}
%license COPYING
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/b64.h
%{_includedir}/%{name}/jwk.h
%{_includedir}/%{name}/jws.h
%{_includedir}/%{name}/jwe.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}-openssl
%{_libdir}/lib%{name}-openssl.so.*

%files -n lib%{name}-openssl-devel
%{_includedir}/%{name}/openssl.h
%{_libdir}/lib%{name}-openssl.so
%{_libdir}/pkgconfig/%{name}-openssl.pc

%files -n lib%{name}-zlib
%{_libdir}/lib%{name}-zlib.so.*

%files -n lib%{name}-zlib-devel
%{_libdir}/lib%{name}-zlib.so
%{_libdir}/pkgconfig/%{name}-zlib.pc

%changelog
* Wed Sep 21 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3-1
- Initial package
