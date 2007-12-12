%define name mp3asm
%define version 0.1.3
%define subversion 1
%define release 1mdk

Name:           %{name}
Summary:        An mpeg 1/2/2.5 audio layer 1,2,3 frame level editor.
Version:        %{version}
Release:        %{release}
License:        GPL
Group:          Sound
URL:            http://sourceforge.net/projects/mp3asm
Source0:        %{name}-%{version}-%{subversion}.tar.bz2
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

