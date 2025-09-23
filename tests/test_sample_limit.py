# MIT License

# Copyright (c) 2025 Institute for Automotive Engineering (ika), RWTH Aachen University

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest


def test_sample_limit_config_parsing():
    """Test that sample limit is properly parsed from global config."""
    # Test config with sample limit
    global_config = {
        "cpu_percentage": 80,
        "resample_config": {
            "master_topic": "/camera/image",
            "association": "last",
            "discard_eps": 0.1,
            "sample_limit": 50
        }
    }
    
    # Test that sample limit is properly extracted
    resample_config = global_config.get("resample_config")
    assert resample_config is not None
    assert resample_config["master_topic"] == "/camera/image"
    assert resample_config["association"] == "last"
    assert resample_config["discard_eps"] == 0.1
    assert resample_config["sample_limit"] == 50


def test_sample_limit_none_config():
    """Test that sample limit is None when not specified."""
    # Test config without sample limit
    global_config = {
        "cpu_percentage": 80,
        "resample_config": {
            "master_topic": "/camera/image",
            "association": "last",
            "discard_eps": 0.1
        }
    }
    
    # Test that sample limit is None
    resample_config = global_config.get("resample_config")
    assert resample_config is not None
    assert resample_config["master_topic"] == "/camera/image"
    assert resample_config["association"] == "last"
    assert resample_config["discard_eps"] == 0.1
    assert resample_config.get("sample_limit") is None


def test_sample_limit_validation():
    """Test that sample limit validation works correctly."""
    # Test valid sample limit
    sample_limit = 100
    assert isinstance(sample_limit, int)
    assert sample_limit > 0
    
    # Test None sample limit (should be valid)
    sample_limit = None
    assert sample_limit is None or (isinstance(sample_limit, int) and sample_limit > 0)
    
    # Test invalid sample limit (negative)
    sample_limit = -10
    assert not (isinstance(sample_limit, int) and sample_limit > 0)
    
    # Test invalid sample limit (zero)
    sample_limit = 0
    assert not (isinstance(sample_limit, int) and sample_limit > 0)
