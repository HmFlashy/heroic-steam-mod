#!/usr/bin/env python3
import json, os, sys

config_path = '/home/masterh/Games/Heroic/Prefixes/Cyberpunk 2077/drive_c/users/steamuser/AppData/Local/CD Projekt Red/Cyberpunk 2077/UserSettings.json'

if not os.path.exists(config_path):
    sys.exit(0)

try:
    with open(config_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    target_settings = {
        '/graphics/presets': {
            'QuickPresets': 'Low',
            'TextureQuality': 'Low',
            'ResolutionScaling': 'DLSS',
            'DLSS': 'Performance',
            'DLSS_NewSharpness': 0.50,
            'FrameGeneration': 'Off',
            'DLSSFrameGen': False,
        },
        '/graphics/raytracing': {
            'RayTracing': False,
            'RayTracedReflections': False,
            'RayTracedSunShadows': False,
            'RayTracedLocalShadows': False,
            'RayTracedLighting': 'Off',
            'RayTracedPathTracing': False,
            'RayTracedPathTracingForPhotoMode': False
        },
        '/graphics/advanced': {
            'ContactShadows': False,
            'FacialTangentUpdates': False,
            'Anisotropy': 4,
            'ShadowMeshQuality': 'Low',
            'LocalShadowsQuality': 'Low',
            'CascadedShadowsRange': 'Low',
            'CascadedShadowsResolution': 'Low',
            'DistantShadowsResolution': 'Low',
            'VolumetricFogResolution': 'Low',
            'VolumetricCloudsQuality': 'Low',
            'MaxDynamicDecals': 'Low',
            'ScreenSpaceReflectionsQuality': 'Off',
            'SubsurfaceScatteringQuality': 'Low',
            'AmbientOcclusion': 'Off',
            'ColorPrecision': 'Medium',
            'GlobaIlluminationRange': 'Low',
            'MirrorQuality': 'Low',
            'LODPreset': 'Low'
        },
        '/graphics/basic': {
            'FilmGrain': False,
            'ChromaticAberration': False,
            'DepthOfField': False,
            'LensFlares': False,
            'MotionBlur': 'Off',
            'Vignette': False
        },
        '/graphics/performance': {
            'CrowdDensity': 'Low'
        },
        '/gameplay/performance': {
            'CrowdDensity': 'Low'
        },
        '/gameplay/misc': {
            'EnableCloudSaves': True,
            'EnableMarketing': False,
            'EnableTelemetry': False
        },
        '/video/display': {
            'Resolution': '1600x900',
            'WindowMode': 'Fullscreen',
            'VSync': 'UI-Settings-Video-QualitySetting-Off',
            'MaximumFPS_OnOff': False
        }
    }

    modified = 0
    for group in data.get('data', []):
        gname = group.get('group_name')
        if gname in target_settings:
            group_targets = target_settings[gname]
            for opt in group.get('options', []):
                oname = opt.get('name')
                if oname in group_targets:
                    new_val = group_targets[oname]
                    if opt.get('value') != new_val:
                        opt['value'] = new_val
                        modified += 1

    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f'[Cyberpunk-Opt] Applied {modified} settings successfully (Low + DLSS Performance).')
except Exception as e:
    print(f'[Cyberpunk-Opt] Error: {e}')
