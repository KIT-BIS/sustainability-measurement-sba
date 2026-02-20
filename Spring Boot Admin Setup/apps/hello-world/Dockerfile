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

VOLUME /tmp

COPY --from=builder /build/target/app.jar /opt/app/app.jar

ENV SPRING_AOT_ENABLED=true

CMD ["bash", "-c", "java $JAVA_OPTS -jar /opt/app/app.jar"]
