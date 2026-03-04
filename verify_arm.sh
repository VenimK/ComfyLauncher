#!/bin/bash
# Apple Silicon ARM64 Verification Script

echo "🔍 Apple Silicon Verification"
echo "=============================="
echo ""

echo "1️⃣  System Architecture:"
ARCH=$(uname -m)
echo "   $ARCH"
if [ "$ARCH" = "arm64" ]; then
    echo "   ✅ Native ARM64"
else
    echo "   ⚠️  Not ARM64 (found: $ARCH)"
fi

echo ""
echo "2️⃣  Python Architecture:"
PYTHON_ARCH=$(python3 -c "import platform; print(platform.machine())")
echo "   $PYTHON_ARCH"
if [ "$PYTHON_ARCH" = "arm64" ]; then
    echo "   ✅ Python is ARM64 native"
else
    echo "   ⚠️  Python is NOT ARM64 (found: $PYTHON_ARCH)"
fi

echo ""
echo "3️⃣  Python Version:"
python3 --version

echo ""
echo "4️⃣  Virtual Environment Check:"
if [ -d "venv" ]; then
    echo "   ✅ Virtual environment exists"
    source venv/bin/activate
    VENV_PYTHON=$(python -c "import platform; print(platform.machine())")
    echo "   venv Python arch: $VENV_PYTHON"
    if [ "$VENV_PYTHON" = "arm64" ]; then
        echo "   ✅ venv is ARM64 native"
    else
        echo "   ⚠️  venv is NOT ARM64"
    fi
else
    echo "   ⚠️  No virtual environment found"
fi

echo ""
echo "5️⃣  PyQt6 Check:"
python3 << 'EOF'
try:
    from PyQt6.QtCore import QSysInfo
    arch = QSysInfo.currentCpuArchitecture()
    print(f"   PyQt6 arch: {arch}")
    if arch == "arm64":
        print("   ✅ PyQt6 is ARM64 native")
    else:
        print(f"   ⚠️  PyQt6 is NOT ARM64 (found: {arch})")
except ImportError:
    print("   ⚠️  PyQt6 not installed")
EOF

echo ""
echo "6️⃣  Dependencies Check:"
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
    echo "   Installed packages:"
    pip list 2>/dev/null | grep -E "PyQt6|psutil|requests|pyobjc" | while read line; do
        echo "   - $line"
    done
fi

echo ""
echo "7️⃣  Rosetta 2 Check:"
ROSETTA_PROCS=$(ps aux | grep -i python | grep -v grep | grep -i translated | wc -l)
if [ "$ROSETTA_PROCS" -gt 0 ]; then
    echo "   ⚠️  WARNING: Found $ROSETTA_PROCS process(es) running under Rosetta 2"
else
    echo "   ✅ No Rosetta 2 translation detected"
fi

echo ""
echo "8️⃣  CPU Information:"
sysctl -n machdep.cpu.brand_string

echo ""
echo "9️⃣  Memory Available:"
MEM_GB=$(sysctl -n hw.memsize | awk '{print $1/1024/1024/1024}')
echo "   Total RAM: ${MEM_GB} GB"

echo ""
echo "🔟 macOS Version:"
sw_vers | grep ProductVersion | awk '{print "   " $0}'

echo ""
echo "=============================="
echo "📊 Summary:"
echo ""

# Overall status
if [ "$ARCH" = "arm64" ] && [ "$PYTHON_ARCH" = "arm64" ] && [ "$ROSETTA_PROCS" -eq 0 ]; then
    echo "✅ FULLY OPTIMIZED FOR APPLE SILICON"
    echo ""
    echo "Your ComfyLauncher is running:"
    echo "  • Native ARM64 architecture"
    echo "  • No Rosetta 2 translation"
    echo "  • Maximum performance"
    echo "  • Optimal battery efficiency"
else
    echo "⚠️  OPTIMIZATION ISSUES DETECTED"
    echo ""
    if [ "$ARCH" != "arm64" ]; then
        echo "  ❌ System is not ARM64"
    fi
    if [ "$PYTHON_ARCH" != "arm64" ]; then
        echo "  ❌ Python is not ARM64 native"
        echo "     Fix: Install ARM64 Python from python.org"
    fi
    if [ "$ROSETTA_PROCS" -gt 0 ]; then
        echo "  ❌ Running under Rosetta 2"
        echo "     Fix: Reinstall with ARM64 Python"
    fi
fi

echo ""
