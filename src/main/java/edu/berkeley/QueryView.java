package edu.berkeley;

import io.dropwizard.views.View;

public class QueryView extends View {

    private final String message;

    public QueryView(String message) {
        super("query.mustache");
        this.message = message;
    }

    public String getMessage() {
        return message;
    }
}
