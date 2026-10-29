Summary:	BASS 2.4 audio library
Summary(pl.UTF-8):	Biblioteka dźwiękowa BASS 2.4
Name:		libbass
Version:	2.4.18.3
Release:	1
License:	non-free, no source (commercial/free for non-commercial use)
Group:		Libraries
#Source0Download: https://www.un4seen.com/bass.html
Source0:	https://www.un4seen.com/files/bass24-linux.zip
# NoSource0-md5:	ab3049b4b30030c2c85f09e708732997
NoSource:	0
URL:		https://www.un4seen.com/bass.html
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.007
BuildRequires:	unzip
ExclusiveArch:	%{ix86} %{x8664} %{arm32_with_hf} aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BASS is an audio library for use in software on several platforms. Its
purpose is to provide developers with powerful and efficient sample,
stream, MOD music, and recording functions. All in a compact DLL that
won't bloat your software.

%description -l pl.UTF-8
BASS to biblioteka dźwiękowa przeznaczona do używania w programach na
kilku platformach. Celem jest dostarczenie w pełni funkcjonalnej i
wydajnej obsługi próbek, strumieni, muzyki MOD i nagrywania. Wszystko
w zwięzłej bibliotece dynamicznej, nie rozdymającej oprogramowania.

%package devel
Summary:	Header files for BASS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki BASS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for BASS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki BASS.

%package apidocs
Summary:	API documentation for BASS library
Summary(pl.UTF-8):	Dokumentacja API biblioteki BASS
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for BASS library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki BASS.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir}}

%ifarch %{ix86}
install -p libs/x86/libbass.so $RPM_BUILD_ROOT%{_libdir}
%endif
%ifarch %{x8664}
install -p libs/x86_64/libbass.so $RPM_BUILD_ROOT%{_libdir}
%endif
%ifarch %{arm}
install -p libs/armhf/libbass.so $RPM_BUILD_ROOT%{_libdir}
%endif
%ifarch aarch64
install -p libs/aarch64/libbass.so $RPM_BUILD_ROOT%{_libdir}
%endif

cp -p c/bass.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc bass.txt
%{_libdir}/libbass.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/bass.h

%files apidocs
%defattr(644,root,root,755)
%doc bass.chm
