%_javapackages_macros
Name:          spec-version-maven-plugin
Version:       1.2
Release:       3.0%{?dist}
Summary:       Spec Version Maven Plugin
License:       CDDL or GPLv2 with exceptions
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/spec-version-maven-plugin-1.2
# tar czf spec-version-maven-plugin-1.2-src-svn.tar.gz spec-version-maven-plugin-1.2
Source0:       %{name}-%{version}-src-svn.tar.gz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# spec-version-maven-plugin package don't include the license file
Source1:       glassfish-LICENSE.txt

BuildRequires: java-devel
BuildRequires: mvn(net.java:jvnet-parent)

BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.codehaus.plexus:plexus-resources)

# test dep
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

BuildRequires: maven-local
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-plugin

BuildArch:     noarch

%description
Maven Plugin to configure APIs version and
specs in a MANIFEST.MF file.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

sed -i "s|mvn|mvn-rpmbuild|" src/main/resources/checkVersion.sh

cp -p %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%mvn_file :%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt