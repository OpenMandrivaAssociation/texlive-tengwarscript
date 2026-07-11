%global tl_name tengwarscript
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.1
Release:	%{tl_revision}.1
Summary:	LaTeX support for using Tengwar fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tengwarscript
License:	lppl1.3a
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tengwarscript.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tengwarscript.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tengwarscript.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides "mid-level" access to tengwar fonts, providing good
quality output. Each tengwar sign is represented by a command, which
will place the sign nicely in relation to previous signs. A
transcription package is available from the package's home page: writing
all those tengwar commands would quickly become untenable. The package
supports the use of a wide variety of tengwar fonts that are available
from the net; metric and map files are provided for all the supported
fonts.

