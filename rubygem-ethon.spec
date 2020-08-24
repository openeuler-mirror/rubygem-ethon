%global gem_name ethon
Name:                rubygem-%{gem_name}
Version:             0.9.0
Release:             1
Summary:             Libcurl wrapper
License:             MIT
URL:                 https://github.com/typhoeus/ethon
Source0:             https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:       ruby(release) rubygems-devel >= 1.3.6 ruby rubygem(rspec) rubygem(ffi) => 1.3.0
BuildRequires:       rubygem(mime-types) => 1.18 rubygem(rack) rubygem(sinatra)
BuildArch:           noarch
%description
Very lightweight libcurl wrapper.

%package doc
Summary:             Documentation for %{name}
Requires:            %{name} = %{version}-%{release}
BuildArch:           noarch
%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
sed -i "/#!\/usr\/bin\/env/d" %{buildroot}/%{gem_instdir}/spec/support/server.rb

%check
pushd .%{gem_instdir}
sed -i -e "/require 'bundler'/ s/^/#/" \
       -e "/Bundler.setup/ s/^/#/" \
       spec/spec_helper.rb
rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Guardfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/ethon.gemspec
%{gem_instdir}/profile
%{gem_instdir}/spec

%changelog
* Thu Aug 20 2020 xiezheng <xiezheng4@huawei.com> - 0.9.0-1
- package init
