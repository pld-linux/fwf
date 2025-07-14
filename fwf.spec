Summary:	Free Widgets Foundation
Summary(pl.UTF-8):	Free Widgets Foundation - wolnodostępna podstawa widgetów
Name:		fwf
Version:	0
Release:	0.1
License:	GPL (?)
Group:		Applications
Source0:	ftp://sunsite.unc.edu/pub/X11/fwf/%{name}.tar.gz
# Source0-md5:	4d0798a388cb6020a5b304256f300578
Patch0:		fwf-ssp.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free Widgets Foundation.

%description -l pl.UTF-8
Free Widgets Foundation - wolnodostępna podstawa widgetów.

%prep
%setup -q -n FWF
%patch -P0 -p1

%build

#cd src
xmkmf
%{__make} Makefiles
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif
