# https://hub.docker.com/_/eclipse-temurin/
# Build stage
FROM maven:3.9-eclipse-temurin-25 AS builder

WORKDIR /build

# Copy pom.xml for dependency resolution
COPY pom.xml ./

# Download dependencies (this layer will be cached if pom.xml doesn't change)
RUN mvn dependency:go-offline

# Copy source code
COPY src ./src

# Build the application
RUN mvn clean package -DskipTests

# Runtime stage
FROM eclipse-temurin:25
# Install curl for health check
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

VOLUME /tmp

COPY --from=builder /build/target/app.jar /opt/app/app.jar

CMD ["bash", "-c", "java $JAVA_OPTS -jar /opt/app/app.jar"]
