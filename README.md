# Idealo Sensor

[![Version](https://img.shields.io/badge/version-0.0.1-green.svg?style=for-the-badge)](#) [![mantained](https://img.shields.io/maintenance/yes/2018.svg?style=for-the-badge)](#)

[![maintainer](https://img.shields.io/badge/maintainer-Goran%20Zunic%20%40panbachi-blue.svg?style=for-the-badge)](https://www.panbachi.de)

## Installation
1. Install this component by copying the 'idealo'-folder to your `/custom_components/`. (Now updated to work on hass>=0.88)
2. Add this to your `configuration.yaml` using the config options below example.
3. **You will need to restart for the component to start working**

```yaml
sensor:
  - platform: idealo
    name: Raspberry
    product_id: 6079508
    description: "Raspberry PI 3 Model B+"
    locale: DE
```

### Options
| key           | default | required | description
|---------------|---------|----------|---
| `name`        |         | yes      | The name of the sensor
| `product_id`  |         | yes      | The ID of the product on idealo
| `description` |         | no       | Description of the product
| `locale`      | DE      | no       | The locale of idealo, may be `AT`, `DE`, `ES`, `FR`, `IT` or `UK` 

## Description
You can find the ID of the product in the URL. For example, if you search on https://www.idealo.de for 
`Raspberry Pi 3 B+` and choose the product, the URL you will be redirected to should be: 
`https://www.idealo.de/preisvergleich/OffersOfProduct/6079508_-3-model-b-raspberry-pi-foundation.html`. So the 
`product_id` is the ID in the URL: `6079508`.   

***

Due to how `custom_components` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding 
this, to resolve it, restart Home-Assistant.

***

# Support me / Follow me
[![Web](https://img.shields.io/badge/www-panbachi.de-blue.svg?style=flat-square&colorB=3d72a8&colorA=333333)](https://www.panbachi.de)
[![Facebook](https://img.shields.io/badge/-%40panbachi.de-blue.svg?style=flat-square&logo=facebook&colorB=3B5998&colorA=eee)](https://www.facebook.com/panbachi.de/)
[![Twitter](https://img.shields.io/badge/-%40panbachi-blue.svg?style=flat-square&logo=twitter&colorB=1DA1F2&colorA=eee)](https://twitter.com/panbachi)
[![Instagram](https://img.shields.io/badge/-%40panbachi.de-blue.svg?style=flat-square&logo=instagram&colorB=E4405F&colorA=eee)](http://instagram.com/panbachi.de)
[![YouTube](https://img.shields.io/badge/-%40panbachi-blue.svg?style=flat-square&logo=youtube&colorB=FF0000&colorA=eee)](https://www.youtube.com/channel/UCO7f2L7ZsDCpOtRfKnPqNow)
