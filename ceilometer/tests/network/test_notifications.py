# -*- encoding: utf-8 -*-
#
# Copyright © 2012 New Dream Network, LLC (DreamHost)
#
# Author: Julien Danjou <julien@danjou.info>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""Tests for ceilometer.network.notifications
"""

import mock

from ceilometer.network import notifications
from ceilometer.tests import base as test

NOTIFICATION_NETWORK_CREATE = {
    u'_context_roles': [u'anotherrole',
                        u'Member'],
    u'_context_read_deleted': u'no',
    u'event_type': u'network.create.end',
    u'timestamp': u'2012-09-27 14:11:27.086575',
    u'_context_tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
    u'payload': {u'network':
                 {u'status': u'ACTIVE',
                  u'subnets': [],
                  u'name': u'abcedf',
                  u'router:external': False,
                  u'tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
                  u'admin_state_up': True,
                  u'shared': False,
                  u'id': u'7fd4eb2f-a38e-4c25-8490-71ca8800c9be'}},
    u'priority': u'INFO',
    u'_context_is_admin': False,
    u'_context_timestamp': u'2012-09-27 14:11:26.924779',
    u'_context_user_id': u'b44b7ce67fc84414a5c1660a92a1b862',
    u'publisher_id': u'network.ubuntu-VirtualBox',
    u'message_id': u'9e839576-cc47-4c60-a7d8-5743681213b1'}


NOTIFICATION_SUBNET_CREATE = {
    u'_context_roles': [u'anotherrole',
                        u'Member'],
    u'_context_read_deleted': u'no',
    u'event_type': u'subnet.create.end',
    u'timestamp': u'2012-09-27 14:11:27.426620',
    u'_context_tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
    u'payload': {
        u'subnet': {
            u'name': u'mysubnet',
            u'enable_dhcp': True,
            u'network_id': u'7fd4eb2f-a38e-4c25-8490-71ca8800c9be',
            u'tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
            u'dns_nameservers': [],
            u'allocation_pools': [{u'start': u'192.168.42.2',
                                   u'end': u'192.168.42.254'}],
            u'host_routes': [],
            u'ip_version': 4,
            u'gateway_ip': u'192.168.42.1',
            u'cidr': u'192.168.42.0/24',
            u'id': u'1a3a170d-d7ce-4cc9-b1db-621da15a25f5'}},
    u'priority': u'INFO',
    u'_context_is_admin': False,
    u'_context_timestamp': u'2012-09-27 14:11:27.214490',
    u'_context_user_id': u'b44b7ce67fc84414a5c1660a92a1b862',
    u'publisher_id': u'network.ubuntu-VirtualBox',
    u'message_id': u'd86dfc66-d3c3-4aea-b06d-bf37253e6116'}


NOTIFICATION_PORT_CREATE = {
    u'_context_roles': [u'anotherrole',
                        u'Member'],
    u'_context_read_deleted': u'no',
    u'event_type': u'port.create.end',
    u'timestamp': u'2012-09-27 14:28:31.536370',
    u'_context_tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
    u'payload': {
        u'port': {
            u'status': u'ACTIVE',
            u'name': u'',
            u'admin_state_up': True,
            u'network_id': u'7fd4eb2f-a38e-4c25-8490-71ca8800c9be',
            u'tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
            u'device_owner': u'',
            u'mac_address': u'fa:16:3e:75:0c:49',
            u'fixed_ips': [{
                u'subnet_id': u'1a3a170d-d7ce-4cc9-b1db-621da15a25f5',
                u'ip_address': u'192.168.42.3'}],
            u'id': u'9cdfeb92-9391-4da7-95a1-ca214831cfdb',
            u'device_id': u''}},
    u'priority': u'INFO',
    u'_context_is_admin': False,
    u'_context_timestamp': u'2012-09-27 14:28:31.438919',
    u'_context_user_id': u'b44b7ce67fc84414a5c1660a92a1b862',
    u'publisher_id': u'network.ubuntu-VirtualBox',
    u'message_id': u'7135b8ab-e13c-4ac8-bc31-75e7f756622a'}


NOTIFICATION_PORT_UPDATE = {
    u'_context_roles': [u'anotherrole',
                        u'Member'],
    u'_context_read_deleted': u'no',
    u'event_type': u'port.update.end',
    u'timestamp': u'2012-09-27 14:35:09.514052',
    u'_context_tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
    u'payload': {
        u'port': {
            u'status': u'ACTIVE',
            u'name': u'bonjour',
            u'admin_state_up': True,
            u'network_id': u'7fd4eb2f-a38e-4c25-8490-71ca8800c9be',
            u'tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
            u'device_owner': u'',
            u'mac_address': u'fa:16:3e:75:0c:49',
            u'fixed_ips': [{
                u'subnet_id': u'1a3a170d-d7ce-4cc9-b1db-621da15a25f5',
                u'ip_address': u'192.168.42.3'}],
            u'id': u'9cdfeb92-9391-4da7-95a1-ca214831cfdb',
            u'device_id': u''}},
    u'priority': u'INFO',
    u'_context_is_admin': False,
    u'_context_timestamp': u'2012-09-27 14:35:09.447682',
    u'_context_user_id': u'b44b7ce67fc84414a5c1660a92a1b862',
    u'publisher_id': u'network.ubuntu-VirtualBox',
    u'message_id': u'07b0a3a1-c0b5-40ab-a09c-28dee6bf48f4'}


NOTIFICATION_NETWORK_EXISTS = {
    u'_context_roles': [u'anotherrole',
                        u'Member'],
    u'_context_read_deleted': u'no',
    u'event_type': u'network.exists',
    u'timestamp': u'2012-09-27 14:11:27.086575',
    u'_context_tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
    u'payload': {u'network':
                 {u'status': u'ACTIVE',
                  u'subnets': [],
                  u'name': u'abcedf',
                  u'router:external': False,
                  u'tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
                  u'admin_state_up': True,
                  u'shared': False,
                  u'id': u'7fd4eb2f-a38e-4c25-8490-71ca8800c9be'}},
    u'priority': u'INFO',
    u'_context_is_admin': False,
    u'_context_timestamp': u'2012-09-27 14:11:26.924779',
    u'_context_user_id': u'b44b7ce67fc84414a5c1660a92a1b862',
    u'publisher_id': u'network.ubuntu-VirtualBox',
    u'message_id': u'9e839576-cc47-4c60-a7d8-5743681213b1'}


NOTIFICATION_ROUTER_EXISTS = {
    u'_context_roles': [u'anotherrole',
                        u'Member'],
    u'_context_read_deleted': u'no',
    u'event_type': u'router.exists',
    u'timestamp': u'2012-09-27 14:11:27.086575',
    u'_context_tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
    u'payload': {u'router':
                 {'status': u'ACTIVE',
                  'external_gateway_info':
                  {'network_id': u'89d55642-4dec-43a4-a617-6cec051393b5'},
                  'name': u'router1',
                  'admin_state_up': True,
                  'tenant_id': u'bb04a2b769c94917b57ba49df7783cfd',
                  'id': u'ab8bb3ed-df23-4ca0-8f03-b887abcd5c23'}},
    u'priority': u'INFO',
    u'_context_is_admin': False,
    u'_context_timestamp': u'2012-09-27 14:11:26.924779',
    u'_context_user_id': u'b44b7ce67fc84414a5c1660a92a1b862',
    u'publisher_id': u'network.ubuntu-VirtualBox',
    u'message_id': u'9e839576-cc47-4c60-a7d8-5743681213b1'}


NOTIFICATION_FLOATINGIP_EXISTS = {
    u'_context_roles': [u'anotherrole',
                        u'Member'],
    u'_context_read_deleted': u'no',
    u'event_type': u'floatingip.exists',
    u'timestamp': u'2012-09-27 14:11:27.086575',
    u'_context_tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
    u'payload': {u'floatingip':
                 {'router_id': None,
                  'tenant_id': u'6e5f9df9b3a249ab834f25fe1b1b81fd',
                  'floating_network_id':
                  u'001400f7-1710-4245-98c3-39ba131cc39a',
                  'fixed_ip_address': None,
                  'floating_ip_address': u'172.24.4.227',
                  'port_id': None,
                  'id': u'2b7cc28c-6f78-4735-9246-257168405de6'}},
    u'priority': u'INFO',
    u'_context_is_admin': False,
    u'_context_timestamp': u'2012-09-27 14:11:26.924779',
    u'_context_user_id': u'b44b7ce67fc84414a5c1660a92a1b862',
    u'publisher_id': u'network.ubuntu-VirtualBox',
    u'message_id': u'9e839576-cc47-4c60-a7d8-5743681213b1'}


NOTIFICATION_FLOATINGIP_UPDATE = {
    u'_context_roles': [u'anotherrole',
                        u'Member'],
    u'_context_read_deleted': u'no',
    u'event_type': u'floatingip.update.start',
    u'timestamp': u'2012-09-27 14:11:27.086575',
    u'_context_tenant_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
    u'payload': {u'floatingip':
                   {u'fixed_ip_address': u'172.24.4.227',
                    u'id': u'a68c9390-829e-4732-bad4-e0a978498cc5',
                    u'port_id': u'e12150f2-885b-45bc-a248-af1c23787d55'}},
    u'priority': u'INFO',
    u'_unique_id': u'e483db017b2341fd9ec314dcda88d3e9',
    u'_context_is_admin': False,
    u'_context_project_id': u'82ed0c40ebe64d0bb3310027039c8ed2',
    u'_context_timestamp': u'2012-09-27 14:11:26.924779',
    u'_context_user_id': u'b44b7ce67fc84414a5c1660a92a1b862',
    u'publisher_id': u'network.ubuntu-VirtualBox',
    u'message_id': u'9e839576-cc47-4c60-a7d8-5743681213b1'}


NOTIFICATION_L3_METER = {
    u'_context_roles': [u'admin'],
    u'_context_read_deleted': u'no',
    u'event_type': u'l3.meter',
    u'timestamp': u'2013-08-22 13:14:06.880304',
    u'_context_tenant_id': None,
    u'payload': {u'first_update': 1377176476,
                 u'bytes': 0,
                 u'label_id': u'383244a7-e99b-433a-b4a1-d37cf5b17d15',
                 u'last_update': 1377177246,
                 u'host': u'precise64',
                 u'tenant_id': u'admin',
                 u'time': 30,
                 u'pkts': 0},
    u'priority': u'INFO',
    u'_context_is_admin': True,
    u'_context_timestamp': u'2013-08-22 13:01:06.614635',
    u'_context_user_id': None,
    u'publisher_id': u'metering.precise64',
    u'message_id': u'd7aee6e8-c7eb-4d47-9338-f60920d708e4',
    u'_unique_id': u'd5a3bdacdcc24644b84e67a4c10e886a',
    u'_context_project_id': None}


class TestNotifications(test.BaseTestCase):
    def test_network_create(self):
        v = notifications.Network(mock.Mock())
        samples = list(v.process_notification(NOTIFICATION_NETWORK_CREATE))
        self.assertEqual(2, len(samples))
        self.assertEqual("network.create", samples[1].name)

    def test_subnet_create(self):
        v = notifications.Subnet(mock.Mock())
        samples = list(v.process_notification(NOTIFICATION_SUBNET_CREATE))
        self.assertEqual(2, len(samples))
        self.assertEqual("subnet.create", samples[1].name)

    def test_port_create(self):
        v = notifications.Port(mock.Mock())
        samples = list(v.process_notification(NOTIFICATION_PORT_CREATE))
        self.assertEqual(2, len(samples))
        self.assertEqual("port.create", samples[1].name)

    def test_port_update(self):
        v = notifications.Port(mock.Mock())
        samples = list(v.process_notification(NOTIFICATION_PORT_UPDATE))
        self.assertEqual(2, len(samples))
        self.assertEqual("port.update", samples[1].name)

    def test_network_exists(self):
        v = notifications.Network(mock.Mock())
        samples = v.process_notification(NOTIFICATION_NETWORK_EXISTS)
        self.assertEqual(1, len(list(samples)))

    def test_router_exists(self):
        v = notifications.Router(mock.Mock())
        samples = v.process_notification(NOTIFICATION_ROUTER_EXISTS)
        self.assertEqual(1, len(list(samples)))

    def test_floatingip_exists(self):
        v = notifications.FloatingIP(mock.Mock())
        samples = list(v.process_notification(NOTIFICATION_FLOATINGIP_EXISTS))
        self.assertEqual(1, len(samples))
        self.assertEqual("ip.floating", samples[0].name)

    def test_floatingip_update(self):
        v = notifications.FloatingIP(mock.Mock())
        samples = list(v.process_notification(NOTIFICATION_FLOATINGIP_UPDATE))
        self.assertEqual(len(samples), 2)
        self.assertEqual(samples[0].name, "ip.floating")

    def test_metering_report(self):
        v = notifications.Bandwidth(mock.Mock())
        samples = list(v.process_notification(NOTIFICATION_L3_METER))
        self.assertEqual(1, len(samples))
        self.assertEqual("bandwidth", samples[0].name)


class TestEventTypes(test.BaseTestCase):

    def test_network(self):
        v = notifications.Network(mock.Mock())
        events = v.event_types
        self.assertIsNotEmpty(events)

    def test_subnet(self):
        v = notifications.Subnet(mock.Mock())
        events = v.event_types
        self.assertIsNotEmpty(events)

    def test_port(self):
        v = notifications.Port(mock.Mock())
        events = v.event_types
        self.assertIsNotEmpty(events)

    def test_router(self):
        self.assertTrue(notifications.Router(mock.Mock()).event_types)

    def test_floatingip(self):
        self.assertTrue(notifications.FloatingIP(mock.Mock()).event_types)

    def test_bandwidth(self):
        self.assertTrue(notifications.Bandwidth(mock.Mock()).event_types)
