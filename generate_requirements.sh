#!/bin/bash
# Script to generate clean requirements.txt
# This prevents system packages from contaminating requirements.txt

echo "Django==4.2.11" > requirements.txt
echo "Clean requirements.txt generated successfully!"
echo "To add more packages, edit requirements.in and run: pip-compile requirements.in"