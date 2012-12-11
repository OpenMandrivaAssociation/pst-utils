%define rname libpst

Summary:	Extracts emails from MS Outlook PST files
Name:   	pst-utils
Version: 	0.5.2
Release: 	%mkrel 5
License:	GPL
Group:		Networking/Mail
URL:		http://alioth.debian.org/projects/libpst/
Source0:	http://alioth.debian.org/download.php/844/libpst-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description
LibPST provides functions in library form for accessing Outlook's
Personal Folders. Included with this library is a program that
will take a PST file and convert it to an mbox format. 

%prep

%setup -q -n %{rname}-%{version}

%build

#make CFLAGS="%{optflags} -Wall -DVERSION=\"%{version}\""
make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m0755 readpst %{buildroot}%{_bindir}/
install -m0755 readpstlog %{buildroot}%{_bindir}/

install -m0644 readpst.1 %{buildroot}%{_mandir}/man1/
install -m0644 readpstlog.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CREDITS ChangeLog FILE-FORMAT* LICENSE TODO
%{_bindir}/*
%{_mandir}/man1/*




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.5.2-5mdv2010.0
+ Revision: 430811
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5.2-4mdv2009.0
+ Revision: 259335
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5.2-3mdv2009.0
+ Revision: 247236
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.5.2-1mdv2008.1
+ Revision: 140737
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-1mdv2007.0
+ Revision: 113933
- Import pst-utils

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 0.5.2-1mdv2007.1
- 0.5.2

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.1-1mdk
- 0.5.1

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3.4-2mdk
- rpmbuildupdated

