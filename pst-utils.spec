%define rname libpst

Summary:	Extracts emails from MS Outlook PST files
Name:   	pst-utils
Version: 	0.5.2
Release: 	%mkrel 1
License:	GPL
Group:		Networking/Mail
URL:		http://alioth.debian.org/projects/libpst/
Source0:	http://alioth.debian.org/download.php/844/libpst-%{version}.tar.bz2

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


