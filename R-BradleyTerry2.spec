#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-BradleyTerry2
Version  : 1.1.2
Release  : 28
URL      : https://cran.r-project.org/src/contrib/BradleyTerry2_1.1-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BradleyTerry2_1.1-2.tar.gz
Summary  : Bradley-Terry Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-brglm
Requires: R-gnm
Requires: R-gtools
Requires: R-lme4
Requires: R-prefmod
Requires: R-qvcalc
BuildRequires : R-brglm
BuildRequires : R-gnm
BuildRequires : R-gtools
BuildRequires : R-lme4
BuildRequires : R-prefmod
BuildRequires : R-qvcalc
BuildRequires : buildreq-R

%description
# BradleyTerry2
[![CRAN\_Status\_Badge](https://www.r-pkg.org/badges/version/BradleyTerry2)](https://cran.r-project.org/package=BradleyTerry2)
[![Travis-CI Build
Status](https://travis-ci.org/hturner/BradleyTerry2.svg?branch=master)](https://travis-ci.org/hturner/BradleyTerry2)
[![AppVeyor Build
Status](https://ci.appveyor.com/api/projects/status/github/hturner/BradleyTerry2?branch=master&svg=true)](https://ci.appveyor.com/project/hturner/BradleyTerry2)

%prep
%setup -q -c -n BradleyTerry2
cd %{_builddir}/BradleyTerry2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589757359

%install
export SOURCE_DATE_EPOCH=1589757359
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BradleyTerry2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BradleyTerry2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BradleyTerry2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc BradleyTerry2 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/BradleyTerry2/CITATION
/usr/lib64/R/library/BradleyTerry2/DESCRIPTION
/usr/lib64/R/library/BradleyTerry2/INDEX
/usr/lib64/R/library/BradleyTerry2/Meta/Rd.rds
/usr/lib64/R/library/BradleyTerry2/Meta/data.rds
/usr/lib64/R/library/BradleyTerry2/Meta/features.rds
/usr/lib64/R/library/BradleyTerry2/Meta/hsearch.rds
/usr/lib64/R/library/BradleyTerry2/Meta/links.rds
/usr/lib64/R/library/BradleyTerry2/Meta/nsInfo.rds
/usr/lib64/R/library/BradleyTerry2/Meta/package.rds
/usr/lib64/R/library/BradleyTerry2/Meta/vignette.rds
/usr/lib64/R/library/BradleyTerry2/NAMESPACE
/usr/lib64/R/library/BradleyTerry2/NEWS.md
/usr/lib64/R/library/BradleyTerry2/R/BradleyTerry2
/usr/lib64/R/library/BradleyTerry2/R/BradleyTerry2.rdb
/usr/lib64/R/library/BradleyTerry2/R/BradleyTerry2.rdx
/usr/lib64/R/library/BradleyTerry2/WORDLIST
/usr/lib64/R/library/BradleyTerry2/data/Rdata.rdb
/usr/lib64/R/library/BradleyTerry2/data/Rdata.rds
/usr/lib64/R/library/BradleyTerry2/data/Rdata.rdx
/usr/lib64/R/library/BradleyTerry2/doc/BradleyTerry.R
/usr/lib64/R/library/BradleyTerry2/doc/BradleyTerry.Rnw
/usr/lib64/R/library/BradleyTerry2/doc/BradleyTerry.pdf
/usr/lib64/R/library/BradleyTerry2/doc/index.html
/usr/lib64/R/library/BradleyTerry2/help/AnIndex
/usr/lib64/R/library/BradleyTerry2/help/BradleyTerry2.rdb
/usr/lib64/R/library/BradleyTerry2/help/BradleyTerry2.rdx
/usr/lib64/R/library/BradleyTerry2/help/aliases.rds
/usr/lib64/R/library/BradleyTerry2/help/paths.rds
/usr/lib64/R/library/BradleyTerry2/html/00Index.html
/usr/lib64/R/library/BradleyTerry2/html/R.css
/usr/lib64/R/library/BradleyTerry2/tests/old-tests/old-tests.R
/usr/lib64/R/library/BradleyTerry2/tests/testthat.R
/usr/lib64/R/library/BradleyTerry2/tests/testthat/outputs/add1.rds
/usr/lib64/R/library/BradleyTerry2/tests/testthat/outputs/drop1.rds
/usr/lib64/R/library/BradleyTerry2/tests/testthat/outputs/flatlizards-BTmodel.rds
/usr/lib64/R/library/BradleyTerry2/tests/testthat/outputs/flatlizards-abilities.rds
/usr/lib64/R/library/BradleyTerry2/tests/testthat/outputs/flatlizards-pred0-new.rds
/usr/lib64/R/library/BradleyTerry2/tests/testthat/outputs/flatlizards-pred0-rainy.rds
/usr/lib64/R/library/BradleyTerry2/tests/testthat/outputs/flatlizards-pred1-rainy.rds
/usr/lib64/R/library/BradleyTerry2/tests/testthat/outputs/flatlizards-residuals.rds
/usr/lib64/R/library/BradleyTerry2/tests/testthat/outputs/nested.rds
/usr/lib64/R/library/BradleyTerry2/tests/testthat/test-BTabilities.R
/usr/lib64/R/library/BradleyTerry2/tests/testthat/test-add1-drop1.R
/usr/lib64/R/library/BradleyTerry2/tests/testthat/test-baseball.R
/usr/lib64/R/library/BradleyTerry2/tests/testthat/test-countsToBinomial.R
/usr/lib64/R/library/BradleyTerry2/tests/testthat/test-flatlizards.R
/usr/lib64/R/library/BradleyTerry2/tests/testthat/test-nested.R
/usr/lib64/R/library/BradleyTerry2/tests/testthat/test-predict.R
