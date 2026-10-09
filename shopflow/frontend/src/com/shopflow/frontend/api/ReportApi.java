package com.shopflow.frontend.api;

import com.shopflow.common.json.Json;
import com.shopflow.common.model.Identifiable;
import com.shopflow.common.model.Product;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/**
 * Calls under /api/reports. The payload is produced by the backend's
 * Python report script; this class only gives it a typed shape.
 */
public class ReportApi {

    /** A product name and the quantity sold. */
    public record TopProduct(String product, int quantity) {
    }

    /** Revenue for one calendar day. */
    public record DailyRevenue(String date, double revenue) {
    }

    /** Typed view of the dashboard summary. */
    public record Summary(
            int productCount,
            int customerCount,
            int orderCount,
            double revenue,
            double inventoryValue,
            List<Product> lowStock,
            Map<String, Integer> statusBreakdown,
            List<TopProduct> topProducts,
            List<DailyRevenue> dailyRevenue,
            String generatedBy,
            long generatedAt) {
    }

    private final ApiClient client;

    public ReportApi(ApiClient client) {
        this.client = client;
    }

    public Summary summary() {
        return parse(client.getObject("/api/reports/summary"));
    }

    public Map<String, Object> health() {
        return client.getObject("/api/reports/health");
    }

    static Summary parse(Map<String, Object> map) {
        Map<String, Integer> breakdown = new LinkedHashMap<>();
        for (Map.Entry<String, Object> entry : Json.nested(map, "statusBreakdown").entrySet()) {
            breakdown.put(entry.getKey(), Identifiable.integer(Json.nested(map, "statusBreakdown"), entry.getKey()));
        }
        List<TopProduct> top = new ArrayList<>();
        for (Map<String, Object> item : Json.mapList(Json.nestedList(map, "topProducts"), m -> m)) {
            top.add(new TopProduct(Identifiable.str(item, "product"), Identifiable.integer(item, "quantity")));
        }
        List<DailyRevenue> daily = new ArrayList<>();
        for (Map<String, Object> item : Json.mapList(Json.nestedList(map, "dailyRevenue"), m -> m)) {
            daily.add(new DailyRevenue(Identifiable.str(item, "date"), Identifiable.dbl(item, "revenue")));
        }
        return new Summary(
                Identifiable.integer(map, "productCount"),
                Identifiable.integer(map, "customerCount"),
                Identifiable.integer(map, "orderCount"),
                Identifiable.dbl(map, "revenue"),
                Identifiable.dbl(map, "inventoryValue"),
                Json.mapList(Json.nestedList(map, "lowStock"), Product::fromJson),
                breakdown,
                top,
                daily,
                Identifiable.str(map, "generatedBy"),
                Identifiable.lng(map, "generatedAt"));
    }
}
