# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from apiclient.discovery import build
from airflow.contrib.hooks.gcp_api_base_hook import GoogleCloudBaseHook


class GoogleCloudSpannerHook(GoogleCloudBaseHook):
    """
    Interact with Google Cloud Spanner. This hook uses the Google Cloud Platform
    connection.
    This object is not threads safe. If you want to make multiple requests
    simultaniously, you will need to create a hook per thread.
    """

    def __init__(self,
                 google_cloud_spanner_conn_id='google_cloud_spanner_default',
                 delegate_to=None):
        super(GoogleCloudSpannerHook, self).__init__(google_cloud_spanner_conn_id, delegate_to)
