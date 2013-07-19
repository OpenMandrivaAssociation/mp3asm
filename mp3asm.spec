%define name mp3asm
%define version 0.1.3
%define subversion 1
%define release %mkrel 5

Name:           %{name}
Summary:        An mpeg 1/2/2.5 audio layer 1,2,3 frame level editor
Version:        0.1.3.1
Release:        1
License:        GPL
Group:          Sound
URL:            http://sourceforge.net/projects/mp3asm
Source0:        https://sourceforge.net/projects/mp3asm/files/mp3asm/0.1.3-1/mp3asm-0.1.3-1.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
MP3ASM allows for cutting, copying, pasting of individual frames, 
correction of common (correctable) errors, removal of bad frames and more. 
Quite useful program for maintaining any mp3 collection.

%prep
%setup -q -n %{name}-0.1

%build
%configure
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf %{buildroot}
%{__install} -D src/mp3asm $RPM_BUILD_ROOT%{_bindir}/mp3asm

%clean
rm -rf %{buildroot}

%files -n %{name}
%defattr(0755,root,root,0755)
%{_bindir}/*
%defattr(0644,root,root,0755)
%doc COPYING README Changelog



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.3-5mdv2011.0
+ Revision: 620399
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.3-4mdv2010.0
+ Revision: 430096
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.1.3-3mdv2009.0
+ Revision: 252921
- rebuild
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.1.3-1mdv2008.1
+ Revision: 130233
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import mp3asm


* Tue Jun 1 2004 Austin Acton <austin@mandrakesoft.org> 0.1.3-1mdk
- from Frederic Guardia <frederic.guardia@wanadoo.fr> :
  - First spec file


