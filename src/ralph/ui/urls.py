# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import redirect_to

from ralph.ui.views import typeahead_roles, unlock_field, logout
from ralph.ui.views.common import (
    BulkEdit,
    Home,
    Scan,
    ScanList,
    ScanStatus,
    ServerMove,
)
from ralph.ui.views.ventures import (
    ReportVenturesDeviceList,
    VenturesAddresses,
    VenturesAsset,
    VenturesComponents,
    VenturesHistory,
    VenturesInfo,
    VenturesRoles,
    VenturesSoftware,
    VenturesScan,
)
from ralph.ui.views.racks import (
    RacksAddDevice,
    RacksAddresses,
    RacksAsset,
    RacksComponents,
    RacksHistory,
    RacksInfo,
    RacksRack,
    ReportRacksDeviceList,
    RacksSoftware,
    RacksScan,
)
from ralph.ui.views.search import (
    ReportSearchDeviceList,
    SearchAddresses,
    SearchAsset,
    SearchComponents,
    SearchDeviceList,
    SearchHistory,
    SearchInfo,
    SearchSoftware,
    SearchScan,
)
from ralph.ui.views.services import (
    ReportServicesDeviceList,
    ServicesAddresses,
    ServicesAsset,
    ServicesComponents,
    ServicesDeviceList,
    ServicesHistory,
    ServicesInfo,
    ServicesScan,
    ServicesSoftware,
)
from ralph.ui.views.networks import (
    NetworksAddresses,
    NetworksAsset,
    NetworksComponents,
    NetworksDeviceList,
    NetworksHistory,
    NetworksInfo,
    NetworksSoftware,
    NetworksAutoscan,
    NetworksScan,
)
from ralph.ui.views.deploy import (
    Deployment,
    PrepareMassDeployment,
    MassDeployment,
)
from ralph.ui.views.ventures import VenturesDeviceList
from ralph.ui.views.racks import RacksDeviceList


urlpatterns = patterns(
    '',
    url(r'^logout/$', login_required(logout), {}, 'logout'),
    url(r'^typeahead/roles/$', login_required(typeahead_roles),
        {}, 'typeahead-roles'),
    url(r'^unlock-field/$',
        login_required(unlock_field), {}, 'unlock-field'),
    url(r'^$', login_required(Home.as_view()), {}, 'home'),

    url(r'^(?P<section>\w+)/([^/]*/)?(?P<details>bulkedit)/$',
        login_required(BulkEdit.as_view()), {}, 'bulkedit'),
    url(r'^(?P<section>\w+)/([^/]*/)?(?P<details>deploy)/(?P<device>\d+)$',
        login_required(Deployment.as_view()), {}, 'deploy'),
    url(r'^(?P<section>\w+)/([^/]*/)?(?P<details>move)/$',
        login_required(ServerMove.as_view()), {}, 'servermove'),

    url(r'^search/$',
        login_required(SearchDeviceList.as_view()), {}, 'search'),
    url(r'^search/(?P<details>info)/(?P<device>\d+)$',
        login_required(SearchInfo.as_view()), {}, 'search'),
    url(r'^search/(?P<details>components)/(?P<device>\d+)$',
        login_required(SearchComponents.as_view()), {}, 'search'),
    url(r'^search/(?P<details>software)/(?P<device>\d+)$',
        login_required(SearchSoftware.as_view()), {}, 'search'),
    url(r'^search/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(SearchAddresses.as_view()), {}, 'search'),
    url(r'^search/(?P<details>history)/(?P<device>\d+)$',
        login_required(SearchHistory.as_view()), {}, 'search'),
    url(r'^search/(?P<details>asset)/(?P<device>\d+)$',
        login_required(SearchAsset.as_view()), {}, 'search'),
    url(r'^search/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportSearchDeviceList.as_view()), {'device': ''}, 'search'),
    url(r'^search/(?P<details>\w*)/(?P<device>)$',
        login_required(SearchDeviceList.as_view()), {}, 'search'),
    url(r'^search/(?P<details>scan)/(?P<device>\d+)/$',
        login_required(SearchScan.as_view()), {}, 'search'),
    url(r'^search/(?P<details>scan)/(?P<address>[\d.]*)/$',
        login_required(SearchScan.as_view()), {}, 'search'),


    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/$',
        login_required(ServicesDeviceList.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<details>info|components|software|addresses|history|scan)/(?P<device>)$',
        login_required(ServicesDeviceList.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<device>\d+)$',
        login_required(ServicesInfo.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<details>info)/(?P<device>\d+)$',
        login_required(ServicesInfo.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<details>components)/(?P<device>\d+)$',
        login_required(ServicesComponents.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<details>software)/(?P<device>\d+)$',
        login_required(ServicesSoftware.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(ServicesAddresses.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<details>history)/(?P<device>\d+)$',
        login_required(ServicesHistory.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<details>asset)/(?P<device>\d+)$',
        login_required(ServicesAsset.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<details>scan)/(?P<device>\d+)$',
        login_required(ServicesScan.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<details>scan)/(?P<address>[\d.]*)$',
        login_required(ServicesScan.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<environment_id>env-\d+)/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportServicesDeviceList.as_view()), {'device': ''}, 'services'),

    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/$',
        login_required(ServicesDeviceList.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<details>info|components|software|addresses|history|scan)/(?P<device>)$',
        login_required(ServicesDeviceList.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<device>\d+)$',
        login_required(ServicesInfo.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<details>info)/(?P<device>\d+)$',
        login_required(ServicesInfo.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<details>components)/(?P<device>\d+)$',
        login_required(ServicesComponents.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<details>software)/(?P<device>\d+)$',
        login_required(ServicesSoftware.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(ServicesAddresses.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<details>history)/(?P<device>\d+)$',
        login_required(ServicesHistory.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<details>asset)/(?P<device>\d+)$',
        login_required(ServicesAsset.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<details>scan)/(?P<device>\d+)$',
        login_required(ServicesScan.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<details>scan)/(?P<address>[\d.]*)$',
        login_required(ServicesScan.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<service_id>ser-\d+)/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportServicesDeviceList.as_view()), {'device': ''}, 'services'),

    url(r'^services/(?P<businessline_id>bl-\d+)/$',
        login_required(ServicesDeviceList.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<details>info|components|software|addresses|history|scan)/(?P<device>)$',
        login_required(ServicesDeviceList.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<device>\d+)$',
        login_required(ServicesInfo.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<details>info)/(?P<device>\d+)$',
        login_required(ServicesInfo.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<details>components)/(?P<device>\d+)$',
        login_required(ServicesComponents.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<details>software)/(?P<device>\d+)$',
        login_required(ServicesSoftware.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(ServicesAddresses.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<details>history)/(?P<device>\d+)$',
        login_required(ServicesHistory.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<details>asset)/(?P<device>\d+)$',
        login_required(ServicesAsset.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<details>scan)/(?P<device>\d+)$',
        login_required(ServicesScan.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<details>scan)/(?P<address>[\d.]*)$',
        login_required(ServicesScan.as_view()), {}, 'services'),
    url(r'^services/(?P<businessline_id>bl-\d+)/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportServicesDeviceList.as_view()), {'device': ''}, 'services'),

    url(r'^services/$',
        login_required(ServicesDeviceList.as_view()), {}, 'services'),
    url(r'^services/(?P<details>info|components|software|addresses|history|scan)/(?P<device>)$',
        login_required(ServicesDeviceList.as_view()), {}, 'services'),
    url(r'^services/(?P<device>\d+)/$',
        login_required(ServicesInfo.as_view()), {}, 'services'),
    url(r'^services/(?P<details>info)/(?P<device>\d+)$',
        login_required(ServicesInfo.as_view()), {}, 'services'),
    url(r'^services/(?P<details>components)/(?P<device>\d+)$',
        login_required(ServicesComponents.as_view()), {}, 'services'),
    url(r'^services/(?P<details>software)/(?P<device>\d+)$',
        login_required(ServicesSoftware.as_view()), {}, 'services'),
    url(r'^services/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(ServicesAddresses.as_view()), {}, 'services'),
    url(r'^services/(?P<details>history)/(?P<device>\d+)$',
        login_required(ServicesHistory.as_view()), {}, 'services'),
    url(r'^services/(?P<details>asset)/(?P<device>\d+)$',
        login_required(ServicesAsset.as_view()), {}, 'services'),
    url(r'^services/(?P<details>scan)/(?P<device>\d+)$',
        login_required(ServicesScan.as_view()), {}, 'services'),
    url(r'^services/(?P<details>scan)/(?P<address>[\d.]*)$',
        login_required(ServicesScan.as_view()), {}, 'services'),
    url(r'^services/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportServicesDeviceList.as_view()), {'device': ''}, 'services'),


    url(r'^ventures/$',
        login_required(VenturesDeviceList.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>info|components|software|addresses|prices|costs|history|asset|discover|cmdb)/(?P<device>)$',
        login_required(VenturesDeviceList.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>)(?P<details>info|components|software|addresses|prices|costs|history|asset|discover|cmdb)/(?P<device>)$',
        login_required(VenturesDeviceList.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportVenturesDeviceList.as_view()), {'device': ''}, 'ventures'),
    url(r'^ventures/(?P<venture>)(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportVenturesDeviceList.as_view()), {'device': ''}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>info)/(?P<device>\d+)$',
        login_required(VenturesInfo.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>components)/(?P<device>\d+)$',
        login_required(VenturesComponents.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>software)/(?P<device>\d+)$',
        login_required(VenturesSoftware.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(VenturesAddresses.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>history)/(?P<device>\d+)$',
        login_required(VenturesHistory.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>asset)/(?P<device>\d+)$',
        login_required(VenturesAsset.as_view()), {}, 'ventures'),

    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>roles)/(?P<role>[-\w]*)$',
        login_required(VenturesRoles.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>scan)/(?P<device>\d+)/$',
        login_required(VenturesScan.as_view()), {}, 'ventures'),
    url(r'^ventures/(?P<venture>[.\w*-]*)/(?P<details>scan)/(?P<address>[\d.]*)/$',
        login_required(VenturesScan.as_view()), {}, 'ventures'),

    url(r'^racks/$',
        login_required(RacksDeviceList.as_view()), {}, 'racks'),
    url(r'^racks/-/rack/$', redirect_to,
        {'url': '/ui/racks/-/info/'}),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>add_device)/(?P<device>)$',
        login_required(RacksAddDevice.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>rack)/(?P<device>)$',
        login_required(RacksRack.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>info)/(?P<device>\d+)$',
        login_required(RacksInfo.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>components)/(?P<device>\d+)$',
        login_required(RacksComponents.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>software)/(?P<device>\d+)$',
        login_required(RacksSoftware.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>addresses)/(?P<device>\d+)$',
        login_required(RacksAddresses.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>history)/(?P<device>\d+)$',
        login_required(RacksHistory.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>asset)/(?P<device>\d+)$',
        login_required(RacksAsset.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>reports)/(?P<report>([a-z][\w_-]*)?)$',
        login_required(ReportRacksDeviceList.as_view()), {'device': ''}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>\w+)/(?P<device>)$',
        login_required(RacksDeviceList.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>scan)/(?P<device>\d+)/$',
        login_required(RacksScan.as_view()), {}, 'racks'),
    url(r'^racks/(?P<rack>[-\w]*)/(?P<details>scan)/(?P<address>[\d.]*)/$',
        login_required(RacksScan.as_view()), {}, 'racks'),

    url(r'^networks/$',
        login_required(NetworksDeviceList.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>info)/$',
        login_required(NetworksInfo.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>components)/(?P<device>\d+)$',
        login_required(NetworksComponents.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>software)/(?P<device>\d+)$',
        login_required(NetworksSoftware.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>addresses)/$',
        login_required(NetworksAddresses.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>history)/(?P<device>\d+)$',
        login_required(NetworksHistory.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>asset)/(?P<device>\d+)$',
        login_required(NetworksAsset.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>autoscan)/$',
        login_required(NetworksAutoscan.as_view()), {'status': 'new'}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>autoscan)/(?P<status>new|changed|dead|buried|all)/$',
        login_required(NetworksAutoscan.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>scan)/(?P<device>\d+)/$',
        login_required(NetworksScan.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>scan)/(?P<address>[\d.]*)/$',
        login_required(NetworksScan.as_view()), {}, 'networks'),
    url(r'^networks/(?P<network_id>[^/]*)/(?P<details>\w+)/(?P<device>)$',
        login_required(NetworksDeviceList.as_view()), {}, 'networks'),

    url(r'^deployment/mass/start/$',
        login_required(PrepareMassDeployment.as_view())),
    url(r'^deployment/mass/define/(?P<deployment>[0-9]+)/$',
        login_required(MassDeployment.as_view())),

    url(r'^scan/list/(?P<scan_type>new|existing)/$',
        login_required(
            ScanList.as_view()), {}, 'scan_list',
        ),
    url(r'^scan/status/(?P<job_id>[a-z0-9-]+)/$',
        login_required(
            ScanStatus.as_view()), {}, 'scan_results',
        ),
    url(r'^scan/status/(?P<address>[0-9.]+)/$',
        login_required(
            ScanStatus.as_view()), {}, 'scan_results',
        ),
    url(r'^scan/(?P<address>[0-9.]+)/$',
        login_required(Scan.as_view()), {}, 'scan'),
)
