# Limpa a tela (opcional, funciona em terminal Linux/macOS)
system("clear")  

start <- Sys.time()  # marca o tempo inicial

################################################################################
lcg_schrage <- function(x0, a = 16807, m = 2147483647, n = 10) {
  cat("--------------------------------------------------------------\n")
  cat("Geração de números pseudoaleatórios usando o método de Schrage\n")
  cat("--------------------------------------------------------------\n")
  cat(sprintf("m = %d, a = %d, x0 = %d, n = %d\n\n", m, a, x0, n))

  q <- m %/% a
  r <- m %% a
  x <- x0
  seq <- vector("list", n)

  for (i in 1:n) {
    x <- a * (x %% q) - r * (x %/% q)
    while (x <= 0) {
      x <- x + m  # ajuste para evitar negativos
    }
    u <- x / m
    seq[[i]] <- list(Xn = x, Un = u)
  }

  # Exibição da tabela sem mostrar a semente
  cat(sprintf("%6s|%9s|%10s\n", "n", "Xn", "Un"))
  cat(strrep("-", 30), "\n")
  for (i in 1:n) {
    cat(sprintf("%6d|%9d|%10.6f\n", i, seq[[i]]$Xn, seq[[i]]$Un))
  }

  cat("\nSequência gerada: ", sapply(seq, function(e) e$Xn), "\n")

  return(seq)
}
################################################################################

# Exercício 1
m <- 19; a <- 7; x0 <- 16; n <- 15  

# Executa
seq <- lcg_schrage(x0, a, m, n)

################################################################################

end <- Sys.time()
tempo <- end - start

