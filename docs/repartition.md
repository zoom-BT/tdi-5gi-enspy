# Répartition détaillée (générée depuis les stubs)

Fonctions à implémenter par membre :

| Membre | Chapitre(s) | Modules | Fonctions | Nb |
|---|---|---|---|---|
| M01 | Ch1, Ch2 | `ch01_intro/numerisation.py`<br>`ch01_intro/profil.py`<br>`ch02_base/interpolation.py` | rgb_vers_gris, extraire_canal, echantillonner, quantifier, taille_stockage_bits<br>profil_ligne, profil_colonne, profil_segment<br>zoom_plus_proche_voisin, zoom_bilineaire, zoom_bicubique, redimensionner | 12 |
| M02 | Ch2 | `ch02_base/histogramme.py`<br>`ch02_base/stats.py` | histogramme, histogramme_normalise, histogramme_cumule, egalisation, egalisation_locale, specification_histogramme<br>luminance, contraste_ecart_type, contraste_min_max, dynamique | 10 |
| M03 | Ch2 | `ch02_base/ponctuel.py`<br>`ch02_base/arithmetique.py` | appliquer_lut, transformation_lineaire, transformation_lineaire_saturation, transformation_par_morceaux, correction_gamma, negatif, transformation_log<br>et_logique, ou_logique, xor_logique, non_logique, addition, soustraction, difference_absolue, multiplication, combinaison_lineaire | 16 |
| M04 | Ch7 | `ch07_binaires/connexite.py`<br>`ch07_binaires/etiquetage.py`<br>`ch07_binaires/freeman.py` | voisins, distance_d4, distance_d8, carte_distances<br>etiqueter_multi_passes, etiqueter_une_passe, etiqueter_contours, proprietes_regions<br>code_freeman, decoder_freeman, suivi_contour | 11 |
| M05 | Ch3 | `ch03_convolution/convolution.py`<br>`ch03_convolution/lissage.py`<br>`ch03_convolution/passe_haut.py` | pad, convolution2d, convolution_partielle, convolution_separable<br>noyau_moyenneur, filtre_moyenneur, noyau_gaussien, filtre_gaussien<br>filtre_passe_haut, accentuation_unsharp | 10 |
| M06 | Ch3, Ch7 | `ch03_convolution/ordre.py`<br>`ch03_convolution/bruit.py`<br>`ch07_binaires/morphologie.py` | filtre_median, filtre_min, filtre_max<br>bruit_poivre_sel, bruit_gaussien, psnr<br>element_structurant, erosion, dilatation, ouverture, fermeture, gradient_interne, gradient_externe, gradient_morphologique | 14 |
| M07 | Ch4 | `ch04_fourier/fft.py`<br>`ch04_fourier/spectre.py` | fft1d, ifft1d, pad_puissance_de_2, fft2d, ifft2d, fftshift, ifftshift<br>module, phase, spectre_log, image_sinus, image_carre, image_impulsions | 13 |
| M08 | Ch4 | `ch04_fourier/filtres_frequentiels.py` | masque_passe_bas_ideal, masque_passe_haut_ideal, masque_gaussien, filtrer_frequentiel, energie_par_rayon, filtre_notch, rehaussement_frequentiel | 7 |
| M09 | Ch5, Ch7 | `ch05_contours/gradient.py`<br>`ch05_contours/laplacien.py`<br>`ch07_binaires/fermeture_contours.py` | derivee_simple, roberts, prewitt, sobel, isotropique, norme_gradient, direction_gradient, seuiller_gradient<br>laplacien, passages_par_zero, log<br>fermer_contours, extremites | 13 |
| M10 | Ch5, Ch7 | `ch05_contours/hough.py`<br>`ch05_contours/canny.py`<br>`ch07_binaires/hysteresis.py` | hough_droites, pics_hough, tracer_droites<br>suppression_non_maxima, canny<br>seuillage_hysteresis | 6 |
| M11 | Ch6 | `ch06_segmentation/seuillage.py`<br>`ch06_segmentation/kmeans.py` | seuillage, multi_seuillage, seuil_moyenne, seuil_milieu_min_max, seuil_iteratif, seuil_otsu, seuillage_adaptatif<br>kmeans, segmenter_kmeans_gris, segmenter_kmeans_couleur | 10 |
| M12 | Ch6 | `ch06_segmentation/split_merge.py`<br>`ch06_segmentation/croissance.py` | est_homogene, division, fusion, split_and_merge<br>croissance_region, croissance_multi_germes, germes_automatiques | 7 |
En plus, M01 a `core/io.py` : lire_pgm, ecrire_pgm, lire_ppm, ecrire_ppm, lire_image, ecrire_image.

Le nombre de fonctions n'est pas la charge : fft1d, hough_droites, split/merge, etiqueter_une_passe et egalisation_locale valent chacune plusieurs petites fonctions. La charge estimée par membre est dans le README (7 à 8,5 pts).
