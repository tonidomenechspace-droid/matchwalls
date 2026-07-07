// Store the original fetch method
const originalFetch = window.fetch;

// Override the fetch method
window.fetch = function() {
    const url = arguments[0];
    const options = arguments[1];

    // Check if the URL matches the Shopify conversation API
    if (url.includes('https://messaging-api.shopifyapps.com/shopify_chat/api/storefront/conversations')) {
        
        let requestBody = null;
        
        // Check if the request has a body
        if (options && options.body) {
            try {
                requestBody = JSON.parse(options.body);
            } catch (error) {
                // Handle error silently
            }
        }

        // Call the original fetch and handle the response
        return originalFetch.apply(this, arguments).then(async (response) => {
            // Clone the response so we can read the body
            const clonedResponse = response.clone();
            
            try {
                const responseData = await clonedResponse.json();
                
                if (response.status === 201 && requestBody && requestBody.conversation) {
                    // Populate the dataLayer with the required structure
                    window.dataLayer = window.dataLayer || [];
                    
                    // Push the structured data into the dataLayer
                    window.dataLayer.push({
                        'event': 'user_subscribed',
                        'user_property': 'client_subscription',
                        'subscribtion_canal': 'chat_inbox',
                        'value': true,
                        'customer_info': requestBody.conversation // Add the entire conversation as part of the payload
                    });
                }

            } catch (error) {
                // Handle error silently
            }

            return response; // Return the original response
        }).catch((error) => {
            throw error;
        });
    }

    // Call the original fetch method for all other requests
    return originalFetch.apply(this, arguments);
};
