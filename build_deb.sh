#!/bin/bash

VERSION="v2.0.0"
PKG_NAME="dataframe"
BUILD_DIR="build/${PKG_NAME}-${VERSION}"

# Clean up old build
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR/DEBIAN"
mkdir -p "$BUILD_DIR/usr/local/bin"

# Copy your Python application
cp DataFrame.py "$BUILD_DIR/usr/local/bin/${PKG_NAME}.py"

# Copy control and maintainer scripts
cp DEBIAN/control "$BUILD_DIR/DEBIAN/"
cp DEBIAN/postinst "$BUILD_DIR/DEBIAN/"
cp DEBIAN/prerm "$BUILD_DIR/DEBIAN/"
cp DEBIAN/postrm "$BUILD_DIR/DEBIAN/"

# Permissions
chmod 0755 "$BUILD_DIR"/DEBIAN/*
chmod 0755 "$BUILD_DIR/usr/local/bin/${PKG_NAME}.py"

# Build the package
dpkg-deb --build "$BUILD_DIR"
