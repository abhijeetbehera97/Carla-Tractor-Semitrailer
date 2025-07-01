# 🚛 Improved and Validated Tractor-Semitrailer Vehicle for CARLA Simulator

This repository provides an improved and validated tractor-semi trailer combination model for the [CARLA Simulator](https://carla.org/), based on the source build of CARLA 0.9.14 using Ubuntu 23.04. It includes fixes to existing blueprint issues, addressing several limitations found in earlier implementations and a complete integration workflow for custom vehicle addition and simulator packaging.

![TractorSemitrailer](TractorSemitrailer.png)

---

## ✨ Features

📏 Realistic Vehicle Dimensions

The tractor and trailer geometries closely match real-world counterparts, improving the validity of simulation data and enabling more accurate comparisons with physical tests.

⚙️ Custom Heavy Vehicle Dynamics

The steering and powertrain systems have been adapted to better reflect the behavior of articulated heavy vehicles.

🧪 Validated with Real-World Data

The vehicle model has been validated using measurement data from a real DAF XF95 truck, ensuring high fidelity in behavior and dynamics.

🧩 Full Source Integration for CARLA 0.9.14

The model is compiled directly into CARLA from source, with support for Ubuntu 23.04 — bypassing the limitations of older builds and making development more accessible.

🛠️ Fully Packaged Simulator 

A distribution-ready version of CARLA with the integrated model can be built and shared easily for simulation and testing use cases.

---

## 🛠️ Getting Started

To use or build this improved vehicle model, follow these summarized steps:

### 1. Clone or Fork

```bash
git clone https://github.com/abhijeetbehera97/Carla_TractorSemitrailer.git
````

---

## 🧱 Building CARLA from Source

> ⚠️ Avoid using virtual environments or `sudo` commands during the Unreal build process unless explicitly instructed.

1. **Install Prerequisites**

Follow [CARLA’s build instructions](https://carla.readthedocs.io/en/0.9.14/build_linux/), but **modify** versions to suit **Ubuntu 23.04**:

```bash
sudo apt-get update && sudo apt-get install wget software-properties-common && sudo add-apt-repository ppa:ubuntu-toolchain-r/test && wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add – && sudo apt-get update
sudo apt-add-repository "deb http://apt.llvm.org/focal/ llvm-toolchain-lunar main" sudo apt-get install build-essential clang-13 lld-13 g++-9 cmake ninja-build libvulkan1 python-is-python3 python-dev-is-python3 python3-dev python3-pip libpng-dev libtiff5-dev libjpeg-dev tzdata sed curl unzip autoconf libtool rsync libxml2-dev git sudo update-alternatives --install /usr/bin/clang++ clang++ /usr/lib/llvm-13/bin/clang++ 180 && sudo update-alternatives --install /usr/bin/clang clang /usr/lib/llvm-13/bin/clang 180
```

> Be careful while copying these commands. Some of the interpreters like clang, lld, g++ have different versions than what is specified on Carla's website. That is because they use a different Ubuntu version. For Ubuntu 23.04 (lunar), we used clang-13, lld-13, g++ -9 . You can find the corresponding packages from https://packages.ubuntu.com/search?keywords=ubuntu-software that suits your Ubuntu version. You should also change the repository address if you are using different ubuntu version. For example, if you are using lunar, you should use this "deb http://apt.llvm.org/lunar/ llvm-toolchain-lunar main".

2. **Install Python 3.7**

* Required for compilation (source must find it at `/usr/local/bin/python3.7`)
* Do **not** use virtualenv during build.

3. **Set Unreal Path**

```bash
export UE4_ROOT=~/UnrealEngine_4.26
```

Add this to `~/.bashrc`, and also manually to:

* `util/BuildTools/BuildCarlaUE4.sh`
* `util/BuildTools/Package.sh`

---

## 🚚 Adding the Tractor-Trailer Model

### Assets & Blueprints

1. **Blueprints**

Place these folders:

```
Unreal/CarlaUE4/Content/Carla/Blueprints/Vehicles/
├── DAFTruck/
└── Trailer/
```

2. **Static Meshes**

Place here (create if missing):

```
Unreal/CarlaUE4/Content/Carla/Static/Vehicles/4Wheeled/
├── DAFTruck/
└── Trailer/
```

> 📌 Verify in Unreal Editor that `Trailer` has 6 functions, especially `Couple Tractor and Trailer` and `SetReverseGear`.

---

## 🐍 Python API demo files

1. Copy `manual_controlSemiTrailer.py` to:

```
PythonAPI/examples/manual_controlSemiTrailer.py
```

2. Run using:

```bash
python3 manual_controlSemiTrailer.py
```

> ✅ You **can** use virtualenv here. Make sure required packages are installed. It will be launch the vehicle in pygame. 

---

## 📦 Packaging

You can package CARLA to make it distributable with your custom vehicle:

* Method 1: Unreal Editor → `File > Package Project > Build Target > CarlaUE4`
* Method 2:

```bash
make project
```

> 🕐 Packaging may take several hours. Output will be in `Dist/`.

---

## 📎 Resources

* [Original Project](https://github.com/DanielAtt2000/Tractor-Trailer-Vehicle-and-Roundabout-Dataset-Carla)
* [Vehicle Mesh Source (modified)](https://github.com/frankeng/CarlaSemiTruckTrailer)
* [CARLA Docs - Add Vehicle Tutorial](https://carla.readthedocs.io/en/0.9.14/tuto_A_add_vehicle/)
* Helpful Videos if you want to create your own vehicle model in Carla:

  * [https://www.youtube.com/watch?v=JwJplj92QoU](https://www.youtube.com/watch?v=JwJplj92QoU)
  * [https://www.youtube.com/watch?v=mHgCuJc\_Zh0](https://www.youtube.com/watch?v=mHgCuJc_Zh0)
  * [https://www.youtube.com/watch?v=c5IkFuJNMXE](https://www.youtube.com/watch?v=c5IkFuJNMXE)
  * [https://www.youtube.com/watch?v=mJufrK7RkeI](https://www.youtube.com/watch?v=mJufrK7RkeI)

---

## 🧾 Citation

If you use this model in your research or development, please cite the following paper:

```bibtex
@inproceedings{behera2025CARLA,
  title={Collision avoidance analysis of an articulated heavy vehicle in CARLA},
  author={Behera, Abhijeet and Kharrazi, Sogol and Frisk, Erik},
  booktitle={The IAVSD International Symposium on Dynamics of Vehicles on Roads and Tracks},
  year={2025}
}
```

---

## 📄 License

This project inherits CARLA’s [MIT License](https://github.com/carla-simulator/carla/blob/master/LICENSE). Please ensure attribution to the original authors when distributing or extending.

---

## 🙌 Acknowledgements

Thanks to:

* [DanielAtt2000](https://github.com/DanielAtt2000) for the initial implementation.
* The CARLA community for forum support.


