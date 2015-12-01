__author__ = 'suksubra'
from rest_framework import serializers
from .models import chassisInfo

class chassisSerializer(serializers.Serializer):
    TIME = serializers.CharField(max_length=200)
    AVERAGE_PACKET_SIZE = serializers.CharField(max_length=200)
    CPU_0_5MIN_AVG_SESSMGR_CPUS = serializers.CharField(max_length=200)
    EDR_SEC = serializers.CharField(max_length=200)
    SESSMGR_ACTIVE_CARDS = serializers.CharField(max_length=200)
    THROUGHPUT_KPPS = serializers.CharField(max_length=200)
    THROUGHPUT_MBPS = serializers.CharField(max_length=200)
    TOTAL_CALLS_CONNECTED_SEC = serializers.CharField(max_length=200)
    TOTAL_CALLS_DISCONNECTED_SEC = serializers.CharField(max_length=200)
    TOTAL_SUBSCRIBERS = serializers.CharField(max_length=200)
    UDR_SEC = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `chassisInfo` instance, given the validated data.
        """
        return chassisInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `chassisInfo` instance, given the validated data.
        """
        instance.TIME = validated_data.get('TIME', instance.TIME)
        instance.AVERAGE_PACKET_SIZE = validated_data.get('AVERAGE_PACKET_SIZE', instance.AVERAGE_PACKET_SIZE)
        instance.CPU_0_5MIN_AVG_SESSMGR_CPUS = validated_data.get('CPU_0_5MIN_AVG_SESSMGR_CPUS', instance.CPU_0_5MIN_AVG_SESSMGR_CPUS)
        instance.EDR_SEC = validated_data.get('EDR_SEC', instance.EDR_SEC)
        instance.SESSMGR_ACTIVE_CARDS = validated_data.get('SESSMGR_ACTIVE_CARDS', instance.SESSMGR_ACTIVE_CARDS)
        instance.THROUGHPUT_KPPS = validated_data.get('THROUGHPUT_KPPS', instance.THROUGHPUT_KPPS)
        instance.THROUGHPUT_MBPS = validated_data.get('THROUGHPUT_MBPS', instance.THROUGHPUT_MBPS)
        instance.TOTAL_CALLS_CONNECTED_SEC = validated_data.get('TOTAL_CALLS_CONNECTED_SEC', instance.TOTAL_CALLS_CONNECTED_SEC)
        instance.TOTAL_CALLS_DISCONNECTED_SEC = validated_data.get('TOTAL_CALLS_DISCONNECTED_SEC', instance.TOTAL_CALLS_DISCONNECTED_SEC)
        instance.TOTAL_SUBSCRIBERS = validated_data.get('TOTAL_SUBSCRIBERS', instance.TOTAL_SUBSCRIBERS)
        instance.UDR_SEC = validated_data.get('UDR_SEC', instance.UDR_SEC)

        instance.save()

        return instance


