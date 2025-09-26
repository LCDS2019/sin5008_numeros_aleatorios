# Função LCG em R
lcg <- function(m, a, c, x0, n) {
  system("clear")  
  start <- Sys.time()   # marca o tempo inicial
  
  cat("--------------------------------------------------------------\n")
  cat("Geração de números pseudoaleatórios usando o método LCG\n")
  cat("--------------------------------------------------------------\n")
  cat(sprintf("m = %d, a = %d, c = %d, x0 = %d, n = %d\n\n", m, a, c, x0, n))
  
  iter <- seq_len(n)
  Xn   <- integer(n)
  Un   <- numeric(n)
  
  x <- x0
  for (i in iter) {
    x      <- (a * x + c) %% m
    Xn[i]  <- x
    Un[i]  <- x / m
  }
  
  # Tabela formatada
  cat(sprintf("%3s | %3s | %5s\n", "n", "Xn", "Un"))
  cat("----------------------\n")
  for (i in iter) {
    cat(sprintf("%3d | %3d | %5.2f\n", i, Xn[i], Un[i]))
  }
  
  cat("\nSequência gerada:", paste(Xn, collapse = ", "), "\n")
  
  end <- Sys.time()     # marca o tempo final
  tempo <- end - start
  cat(sprintf("\nTempo total de execução:", as.numeric(tempo, units="secs")))
  
  invisible(data.frame(iter = iter, Xn = Xn, Un = Un, check.names = FALSE))
}

# Exemplo
m = 9
a = 2
c = 1
x0 = 1
n = 15 

# Exercício 2
#m = 10
#a = 7
#c = 7
#x0 = 1
#n = 15  

# Exercício 3 - Park & Miller (1988)
m = 2**31-1; a = 7**5; c = 0; x0 = 1; n = 15  

seq <- lcg(m, a, c, x0, n)
