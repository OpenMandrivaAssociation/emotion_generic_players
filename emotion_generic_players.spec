Summary:	Emotion generic players
Name:		emotion_generic_players
Version:	1.10.0
Release:	1
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.org/rel/libs/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(emotion)
BuildRequires:	pkgconfig(libvlc)

%description
These are binary players for Emotion using the "generic" module.

Emotion supports multiple modules provided as shared-objects under
PREFIX/lib/emotion/modules, making it extensible. However these
live in the same process as the application, thus problems handling
the media may crash or halt the application. Unfortunately media
handling is very error prone due multiple sources, sinks, decoders et
al, each with their own level of stability.

To solve this, Emotion ships with a "generic" module that is a
layer to talk to another process, the "player", using pipes and shared
memory (shm). If this external process dies, the main application
remains working (without any media, of course). Thus it is safer and
has some nice side effects such as avoiding bringing in many libraries to
decode media, saving memory in the application process, etc.

A secondary benefit is that the generic player is a separate process
and does not link with the user application code or EFL, avoiding
license conflicts. Many decoding libraries or elements exist with
conflicting licenses with GPL, LGPL or even proprietary code.

%files
%doc AUTHORS COPYING README
%{_libdir}/emotion/generic_players/*/vlc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

