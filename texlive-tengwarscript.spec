Name:		texlive-tengwarscript
Version:	34594
Release:	2
Summary:	LaTeX support for using Tengwar fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tengwarscript
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tengwarscript.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tengwarscript.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tengwarscript.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides "mid-level" access to tengwar fonts,
providing good quality output. Each tengwar sign is represented
by a command, which will place the sign nicely in relation to
previous signs. A transcription package is available from the
package's home page: writing all those tengwar commands would
quickly become untenable. The package supports the use of a
wide variety of tengwar fonts that are available from the net;
metric and map files are provided for all the supported fonts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/tengwarscript
%{_texmfdistdir}/fonts/map/dvips/tengwarscript
%{_texmfdistdir}/fonts/tfm/public/tengwarscript
%{_texmfdistdir}/fonts/vf/public/tengwarscript
%{_texmfdistdir}/tex/latex/tengwarscript
%doc %{_texmfdistdir}/doc/latex/tengwarscript
#- source
%doc %{_texmfdistdir}/source/latex/tengwarscript

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
