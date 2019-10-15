# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class OperationOrigin(str, Enum):

    user = "user"
    system = "system"
    usersystem = "user,system"


class AggregationType(str, Enum):

    average = "Average"
    total = "Total"


class NodeStatus(str, Enum):

    unused = "unused"
    used = "used"


class OnboardingStatus(str, Enum):

    not_on_boarded = "notOnBoarded"
    on_boarded = "onBoarded"
    on_boarding_failed = "onBoardingFailed"
    on_boarding = "onBoarding"


class DiskIndependenceMode(str, Enum):

    persistent = "persistent"
    independent_persistent = "independent_persistent"
    independent_nonpersistent = "independent_nonpersistent"


class NICType(str, Enum):

    e1000 = "E1000"
    e1000_e = "E1000E"
    pcnet32 = "PCNET32"
    vmxnet = "VMXNET"
    vmxnet2 = "VMXNET2"
    vmxnet3 = "VMXNET3"


class PrivateCloudResourceType(str, Enum):

    microsoft_vmware_cloud_simpleprivate_clouds = "Microsoft.VMwareCloudSimple/privateClouds"


class UsageCount(str, Enum):

    count = "Count"
    bytes = "Bytes"
    seconds = "Seconds"
    percent = "Percent"
    count_per_second = "CountPerSecond"
    bytes_per_second = "BytesPerSecond"


class GuestOSType(str, Enum):

    linux = "linux"
    windows = "windows"
    other = "other"


class VirtualMachineStatus(str, Enum):

    running = "running"
    suspended = "suspended"
    poweredoff = "poweredoff"
    updating = "updating"
    deallocating = "deallocating"
    deleting = "deleting"


class StopMode(str, Enum):

    reboot = "reboot"
    suspend = "suspend"
    shutdown = "shutdown"
    poweroff = "poweroff"