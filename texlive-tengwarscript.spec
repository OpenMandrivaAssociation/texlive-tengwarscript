# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/tengwarscript
# catalog-date 2007-05-24 10:43:22 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-tengwarscript
Version:	1.3
Release:	1
Summary:	LaTeX support for using Tengwar fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tengwarscript
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tengwarscript.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tengwarscript.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tengwarscript.source.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/tengwarscript/tengwaralt.enc
%{_texmfdistdir}/fonts/enc/dvips/tengwarscript/tengwarcap.enc
%{_texmfdistdir}/fonts/enc/dvips/tengwarscript/tengwarscript.enc
%{_texmfdistdir}/fonts/map/dvips/tengwarscript/tengwarscript.map
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/Elfica32.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/Parmaite.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/Parmaite_alt.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/Parmaite_full.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarFormal12.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarFormalA12.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarFormal_full.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarGothika050.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarNoldor.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarNoldorAlt.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarNoldorCapitals1.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarNoldorCapitals2.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarNoldor_full.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarQuenya.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarQuenyaAlt.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarQuenyaCapitals1.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarQuenyaCapitals2.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarQuenya_full.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarSindarin.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarSindarinAlt.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarSindarinCapitals1.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarSindarinCapitals2.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarSindarin_full.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/TengwarTelerin.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/UnicodeParmaite.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tngan.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tngan_full.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tngana.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tnganab.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tnganabi.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tnganai.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tnganb.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tnganb_full.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tnganbi.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tnganbi_full.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tngani.tfm
%{_texmfdistdir}/fonts/tfm/public/tengwarscript/tngani_full.tfm
%{_texmfdistdir}/fonts/vf/public/tengwarscript/Parmaite_full.vf
%{_texmfdistdir}/fonts/vf/public/tengwarscript/TengwarFormal_full.vf
%{_texmfdistdir}/fonts/vf/public/tengwarscript/TengwarNoldor_full.vf
%{_texmfdistdir}/fonts/vf/public/tengwarscript/TengwarQuenya_full.vf
%{_texmfdistdir}/fonts/vf/public/tengwarscript/TengwarSindarin_full.vf
%{_texmfdistdir}/fonts/vf/public/tengwarscript/tngan_full.vf
%{_texmfdistdir}/fonts/vf/public/tengwarscript/tnganb_full.vf
%{_texmfdistdir}/fonts/vf/public/tengwarscript/tnganbi_full.vf
%{_texmfdistdir}/fonts/vf/public/tengwarscript/tngani_full.vf
%{_texmfdistdir}/tex/latex/tengwarscript/annatar.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/annatarbold.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/annatarbolditalic.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/annataritalic.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/elfica.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/formal.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/gothika.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/noldor.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/noldorcapI.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/noldorcapII.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/parmaite.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/quenya.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/quenyacapI.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/quenyacapII.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/sindarin.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/sindarincapI.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/sindarincapII.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/teleri.cfg
%{_texmfdistdir}/tex/latex/tengwarscript/tengwarscript.sty
%{_texmfdistdir}/tex/latex/tengwarscript/unicodeparmaite.cfg
%doc %{_texmfdistdir}/doc/latex/tengwarscript/COPYING
%doc %{_texmfdistdir}/doc/latex/tengwarscript/README
%doc %{_texmfdistdir}/doc/latex/tengwarscript/quetta.eps
%doc %{_texmfdistdir}/doc/latex/tengwarscript/quetta.pdf
%doc %{_texmfdistdir}/doc/latex/tengwarscript/tengfonts.pdf
%doc %{_texmfdistdir}/doc/latex/tengwarscript/tengfonts.tex
%doc %{_texmfdistdir}/doc/latex/tengwarscript/tengtest.pdf
%doc %{_texmfdistdir}/doc/latex/tengwarscript/tengtest.tex
%doc %{_texmfdistdir}/doc/latex/tengwarscript/tengwarscript.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tengwarscript/tengwarscript.dtx
%doc %{_texmfdistdir}/source/latex/tengwarscript/tengwarscript.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
