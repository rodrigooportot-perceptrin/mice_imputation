La imputación multivariable por ecuaciones encadenadas es un enfoque avanzado para la imputación de
datos faltantes en donde se utilizan múltiples ecuaciones de regresión aplicadas de forma iterativa. Este método estima los valores faltantes utilizando las variables disponibles en el conjunto de datos como predictores en un modelo de regresión, adaptado a la naturaleza de cada variable.

Respecto a la versión 2025, el proceso de imputación fue modificado, aprovechando de mejor manera las fortalezas de MICE. A grandes rasgos, la imputación ahora se ejecuta para cada dimensión de forma completa, utilizando todos los subindicadores que la componen para generar los valores faltantes de esta. A su vez, se añaden columnas auxiliares que varían según la dimensión, tales como población, PIB per cápita, crecimiento promedio del PIB durante los últimos 10 años, índice de desarrollo humano, entre otros. 

Las columnas auxiliares comparten elementos temáticos con la dimensión en cuestión, mientras que otros son indicadores de desarrollo general de un país. Estos valores auxiliares permiten apoyar la imputación de manera general y en casos específicos, como sucede con los países con una mayor ausencia transversal de datos al observar una dimensión completa o el conjunto de datos del ILIA en su totalidad. 


En términos mecánicos, la ejecución lleva a cabo 10 iteraciones distintas, cada una con una semilla fija para una aleatoriedad reproducible (números enteros del 0 al 9). Dentro de estas 10 iteraciones, cada una posee otras 100 iteraciones de MICE, que al terminar, entregan los valores sintéticos que sustituyen los casos de ausencia. Finalmente se promedian las 10 iteraciones iniciales, obteniendo el valor final para cada elemento ausente en la dimensión. Esta aproximación permite analizar la estabilidad de las imputaciones en cada subindicador, los casos con mayor divergencia o inestabilidad, entre otros aspectos.


