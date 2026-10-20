@echo off
chcp 65001 > nul
echo ========================================================
echo   multiCAD-MCP - Publicacion al Fork de jmcaamanog
echo ========================================================
echo.
echo Verificando configuracion de remote origin...
git remote -v
echo.
echo 1. Publicando rama main (AECO ConTech Edition completa)...
git push -u origin main
echo.
echo 2. Publicando ramas atomicas para Pull Requests (pr/01 a pr/18)...
git push origin pr/01-fix-fastmcp-and-security
git push origin pr/02-cli-entrypoint-and-parsers
git push origin pr/03-1click-desktop-installer
git push origin pr/04-headless-ezdxf-engine
git push origin pr/05-cad-qa-audit-purge-and-ci
git push origin pr/06-view-camera-control
git push origin pr/07-human-in-the-loop
git push origin pr/08-vector-pdf-plotter
git push origin pr/09-bim-metadata-xdata
git push origin pr/10-xref-raster-manager
git push origin pr/11-drawing-inspector-and-viewer
git push origin pr/12-smart-annotations
git push origin pr/13-offset-and-fillet
git push origin pr/14-boundary-and-join
git push origin pr/15-geometry-snapping-intersections
git push origin pr/16-paperspace-layout-generator
git push origin pr/17-advanced-hatch-patterns
git push origin pr/18-find-and-replace-text
echo.
echo ========================================================
echo   Publicacion completada con exito en tu fork!
echo ========================================================
pause
