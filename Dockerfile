FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /app
COPY . .
RUN dotnet publish BSL.v41.General/BSL.v41.General.csproj -c Release -o /out

FROM mcr.microsoft.com/dotnet/runtime:8.0
WORKDIR /app
COPY --from=build /out .
EXPOSE 9339
ENV TELEGRAM_TOKEN=""
ENV ADMIN_ID=""
ENTRYPOINT ["dotnet", "BSL.v41.General.dll"]
