# Browse API (vv1.20.4)

**Base URL:** `https://api.ebay.com{basePath}`

### `GET` `/item/`
- **operationId:** `getItems`
- **Summary:** This method retrieves the details about specific items that buyers need to make a purchasing decision.<br><br><span class="tablenote"><b>Note:</b> ...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/item/get_item_by_legacy_id`
- **operationId:** `getItemByLegacyId`
- **Summary:** This method is a bridge between the eBay legacy APIs, such as <b>Shopping</b> and <b>Finding</b>, and the eBay Buy APIs. There are differences betw...
- **Required Path Params:** None
- **Required Query Params:** `legacy_item_id`

### `GET` `/item/get_items_by_item_group`
- **operationId:** `getItemsByItemGroup`
- **Summary:** This method retrieves details about individual items in an item group. An item group is an item that has various aspect differences, such as color,...
- **Required Path Params:** None
- **Required Query Params:** `item_group_id`

### `GET` `/item/{item_id}`
- **operationId:** `getItem`
- **Summary:** This method retrieves the details of a specific item, such as description, price, category, all item aspects, condition, return policies, seller fe...
- **Required Path Params:** `item_id`
- **Required Query Params:** None

### `POST` `/item/{item_id}/check_compatibility`
- **operationId:** `checkCompatibility`
- **Summary:** This method checks if a product is compatible with the specified item. You can use this method to check the compatibility of cars, trucks, and moto...
- **Required Path Params:** `item_id`
- **Required Query Params:** None

### `GET` `/item_summary/search`
- **operationId:** `search`
- **Summary:** This method searches for eBay items by various query parameters and retrieves summaries of the items. You can search by keyword, category, eBay pro...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/item_summary/search_by_image`
- **operationId:** `searchByImage`
- **Summary:** This method searches for eBay items based on a image and retrieves summaries of the items. You pass in a Base64 image in the request payload and ca...
- **Required Path Params:** None
- **Required Query Params:** None

*Total endpoints in Browse API: 7*

---

# Inventory API (v1.18.4)

**Base URL:** `https://api.ebay.com{basePath}`

### `POST` `/bulk_create_offer`
- **operationId:** `bulkCreateOffer`
- **Summary:** This call creates multiple offers (up to 25) for specific inventory items on a specific eBay marketplace. Although it is not a requirement for the ...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/bulk_create_or_replace_inventory_item`
- **operationId:** `bulkCreateOrReplaceInventoryItem`
- **Summary:** <span class="tablenote"><strong>Note:</strong> Please note that any eBay listing created using the Inventory API cannot be revised or relisted usin...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/bulk_get_inventory_item`
- **operationId:** `bulkGetInventoryItem`
- **Summary:** This call retrieves up to 25 inventory item records. The SKU value of each inventory item record to retrieve is specified in the request payload.<b...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/bulk_migrate_listing`
- **operationId:** `bulkMigrateListing`
- **Summary:** This call is used to convert existing eBay Listings to the corresponding Inventory API objects. If an eBay listing is successfully migrated to the ...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/bulk_publish_offer`
- **operationId:** `bulkPublishOffer`
- **Summary:** <span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reach...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/bulk_update_price_quantity`
- **operationId:** `bulkUpdatePriceQuantity`
- **Summary:** This call is used by the seller to update the total ship-to-home quantity of one inventory item, and/or to update the price and/or quantity of one ...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/inventory_item`
- **operationId:** `getInventoryItems`
- **Summary:** This call retrieves all inventory item records defined for the seller's account. The <strong>limit</strong> query parameter allows the seller to co...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/inventory_item/{sku}`
- **operationId:** `getInventoryItem`
- **Summary:** This call retrieves the inventory item record for a given SKU. The SKU value is passed in at the end of the call URI. There is no request payload f...
- **Required Path Params:** `sku`
- **Required Query Params:** None

### `PUT` `/inventory_item/{sku}`
- **operationId:** `createOrReplaceInventoryItem`
- **Summary:** <span class="tablenote"><strong>Note:</strong> Please note that any eBay listing created using the Inventory API cannot be revised or relisted usin...
- **Required Path Params:** `sku`
- **Required Query Params:** None

### `DELETE` `/inventory_item/{sku}`
- **operationId:** `deleteInventoryItem`
- **Summary:** This call is used to delete an inventory item record associated with a specified SKU. A successful call will not only delete that inventory item re...
- **Required Path Params:** `sku`
- **Required Query Params:** None

### `GET` `/inventory_item/{sku}/product_compatibility`
- **operationId:** `getProductCompatibility`
- **Summary:** This call is used by the seller to retrieve the list of products that are compatible with the inventory item. The SKU value for the inventory item ...
- **Required Path Params:** `sku`
- **Required Query Params:** None

### `PUT` `/inventory_item/{sku}/product_compatibility`
- **operationId:** `createOrReplaceProductCompatibility`
- **Summary:** This call is used by the seller to create or replace a list of products that are compatible with the inventory item. The inventory item is identifi...
- **Required Path Params:** `sku`
- **Required Query Params:** None

### `DELETE` `/inventory_item/{sku}/product_compatibility`
- **operationId:** `deleteProductCompatibility`
- **Summary:** This call is used by the seller to delete the list of products that are compatible with the inventory item that is associated with the compatible p...
- **Required Path Params:** `sku`
- **Required Query Params:** None

### `GET` `/inventory_item_group/{inventoryItemGroupKey}`
- **operationId:** `getInventoryItemGroup`
- **Summary:** This call retrieves the inventory item group for a given <strong>inventoryItemGroupKey</strong> value. The <strong>inventoryItemGroupKey</strong> v...
- **Required Path Params:** `inventoryItemGroupKey`
- **Required Query Params:** None

### `PUT` `/inventory_item_group/{inventoryItemGroupKey}`
- **operationId:** `createOrReplaceInventoryItemGroup`
- **Summary:** <span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reach...
- **Required Path Params:** `inventoryItemGroupKey`
- **Required Query Params:** None

### `DELETE` `/inventory_item_group/{inventoryItemGroupKey}`
- **operationId:** `deleteInventoryItemGroup`
- **Summary:** This call deletes the inventory item group for a given <strong>inventoryItemGroupKey</strong> value.
- **Required Path Params:** `inventoryItemGroupKey`
- **Required Query Params:** None

### `GET` `/listing/{listingId}/sku/{sku}/locations`
- **operationId:** `getSkuLocationMapping`
- **Summary:** This method allows sellers to retrieve the locations mapped to a specific SKU within a listing.<br><br>The <b>listingId</b> and <b>sku</b> of the l...
- **Required Path Params:** `listingId`, `sku`
- **Required Query Params:** None

### `PUT` `/listing/{listingId}/sku/{sku}/locations`
- **operationId:** `createOrReplaceSkuLocationMapping`
- **Summary:** This method allows sellers to map multiple fulfillment center locations to single-SKU listing, or to a single SKU within a multiple-variation listi...
- **Required Path Params:** `listingId`, `sku`
- **Required Query Params:** None

### `DELETE` `/listing/{listingId}/sku/{sku}/locations`
- **operationId:** `deleteSkuLocationMapping`
- **Summary:** This method allows sellers to remove all location mappings associated with a specific SKU within a listing.<br><br>The <b>listingId</b> and <b>sku<...
- **Required Path Params:** `listingId`, `sku`
- **Required Query Params:** None

### `GET` `/location`
- **operationId:** `getInventoryLocations`
- **Summary:** This call retrieves all defined details for every inventory location associated with the seller's account. There are no required parameters for thi...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/location/{merchantLocationKey}`
- **operationId:** `getInventoryLocation`
- **Summary:** This call retrieves all defined details of the inventory location that is specified by the <b>merchantLocationKey</b> path parameter.<p>A successfu...
- **Required Path Params:** `merchantLocationKey`
- **Required Query Params:** None

### `POST` `/location/{merchantLocationKey}`
- **operationId:** `createInventoryLocation`
- **Summary:** <p>Use this call to create a new inventory location. In order to create and publish an offer (and create an eBay listing), a seller must have at le...
- **Required Path Params:** `merchantLocationKey`
- **Required Query Params:** None

### `DELETE` `/location/{merchantLocationKey}`
- **operationId:** `deleteInventoryLocation`
- **Summary:** <p>This call deletes the inventory location that is specified in the <code>merchantLocationKey</code> path parameter. Note that deleting a location...
- **Required Path Params:** `merchantLocationKey`
- **Required Query Params:** None

### `POST` `/location/{merchantLocationKey}/disable`
- **operationId:** `disableInventoryLocation`
- **Summary:** <p>This call disables the inventory location that is specified in the <code>merchantLocationKey</code> path parameter. Sellers can not load/modify ...
- **Required Path Params:** `merchantLocationKey`
- **Required Query Params:** None

### `POST` `/location/{merchantLocationKey}/enable`
- **operationId:** `enableInventoryLocation`
- **Summary:** <p>This call enables a disabled inventory location that is specified in the <code>merchantLocationKey</code> path parameter. Once a disabled locati...
- **Required Path Params:** `merchantLocationKey`
- **Required Query Params:** None

### `POST` `/location/{merchantLocationKey}/update_location_details`
- **operationId:** `updateInventoryLocation`
- **Summary:** <p>Use this call to update location details for an existing inventory location. Specify the inventory location you want to update using the <b>merc...
- **Required Path Params:** `merchantLocationKey`
- **Required Query Params:** None

### `GET` `/offer`
- **operationId:** `getOffers`
- **Summary:** This call retrieves all existing offers for the specified SKU value. The seller has the option of limiting the offers that are retrieved to a speci...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/offer`
- **operationId:** `createOffer`
- **Summary:** This call creates an offer for a specific inventory item on a specific eBay marketplace. It is up to the sellers whether they want to create a comp...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/offer/get_listing_fees`
- **operationId:** `getListingFees`
- **Summary:** This call is used to retrieve the expected listing fees for up to 250 unpublished offers. An array of one or more <strong>offerId</strong> values a...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/offer/publish_by_inventory_item_group`
- **operationId:** `publishOfferByInventoryItemGroup`
- **Summary:** <span class="tablenote"><strong>Note:</strong> Please note that any eBay listing created using the Inventory API cannot be revised or relisted usin...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/offer/withdraw_by_inventory_item_group`
- **operationId:** `withdrawOfferByInventoryItemGroup`
- **Summary:** This call is used to end a multiple-variation eBay listing that is associated with the specified inventory item group. This call only ends multiple...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/offer/{offerId}`
- **operationId:** `getOffer`
- **Summary:** This call retrieves a specific published or unpublished offer. The unique identifier of the offer (<strong>offerId</strong>) is passed in at the en...
- **Required Path Params:** `offerId`
- **Required Query Params:** None

### `PUT` `/offer/{offerId}`
- **operationId:** `updateOffer`
- **Summary:** This call updates an existing offer. An existing offer may be in published state (active eBay listing), or in an unpublished state and yet to be pu...
- **Required Path Params:** `offerId`
- **Required Query Params:** None

### `DELETE` `/offer/{offerId}`
- **operationId:** `deleteOffer`
- **Summary:** If used against an unpublished offer, this call will permanently delete that offer. In the case of a published offer (or live eBay listing), a succ...
- **Required Path Params:** `offerId`
- **Required Query Params:** None

### `POST` `/offer/{offerId}/publish`
- **operationId:** `publishOffer`
- **Summary:** <span class="tablenote"><strong>Note:</strong> Each listing can be revised up to 250 times in one calendar day. If this revision threshold is reach...
- **Required Path Params:** `offerId`
- **Required Query Params:** None

### `POST` `/offer/{offerId}/withdraw`
- **operationId:** `withdrawOffer`
- **Summary:** This call is used to end a single-variation listing that is associated with the specified offer. This call is used in place of the <strong>deleteOf...
- **Required Path Params:** `offerId`
- **Required Query Params:** None

*Total endpoints in Inventory API: 36*

---

# Fulfillment API (vv1.20.7)

**Base URL:** `https://api.ebay.com{basePath}`

### `GET` `/order`
- **operationId:** `getOrders`
- **Summary:** Use this method to search for and retrieve one or more orders based on their creation date, last modification date, or fulfillment status using the...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/order/{orderId}`
- **operationId:** `getOrder`
- **Summary:** Use this call to retrieve the contents of an order based on its unique identifier, <i>orderId</i>. This value was returned in the <b> getOrders</b>...
- **Required Path Params:** `orderId`
- **Required Query Params:** None

### `GET` `/order/{orderId}/shipping_fulfillment`
- **operationId:** `getShippingFulfillments`
- **Summary:** Use this call to retrieve the contents of all fulfillments currently defined for a specified order based on the order's unique identifier, <b>order...
- **Required Path Params:** `orderId`
- **Required Query Params:** None

### `POST` `/order/{orderId}/shipping_fulfillment`
- **operationId:** `createShippingFulfillment`
- **Summary:** When you group an order's line items into one or more packages, each package requires a corresponding plan for handling, addressing, and shipping; ...
- **Required Path Params:** `orderId`
- **Required Query Params:** None

### `GET` `/order/{orderId}/shipping_fulfillment/{fulfillmentId}`
- **operationId:** `getShippingFulfillment`
- **Summary:** Use this call to retrieve the contents of a fulfillment based on its unique identifier, <b>fulfillmentId</b> (combined with the associated order's ...
- **Required Path Params:** `fulfillmentId`, `orderId`
- **Required Query Params:** None

### `POST` `/order/{order_id}/issue_refund`
- **operationId:** `issueRefund`
- **Summary:** Issue Refund
- **Required Path Params:** `order_id`
- **Required Query Params:** None

### `GET` `/payment_dispute/{payment_dispute_id}`
- **operationId:** `getPaymentDispute`
- **Summary:** Get Payment Dispute Details
- **Required Path Params:** `payment_dispute_id`
- **Required Query Params:** None

### `POST` `/payment_dispute/{payment_dispute_id}/accept`
- **operationId:** `acceptPaymentDispute`
- **Summary:** Accept Payment Dispute
- **Required Path Params:** `payment_dispute_id`
- **Required Query Params:** None

### `GET` `/payment_dispute/{payment_dispute_id}/activity`
- **operationId:** `getActivities`
- **Summary:** Get Payment Dispute Activity
- **Required Path Params:** `payment_dispute_id`
- **Required Query Params:** None

### `POST` `/payment_dispute/{payment_dispute_id}/add_evidence`
- **operationId:** `addEvidence`
- **Summary:** Add an Evidence File
- **Required Path Params:** `payment_dispute_id`
- **Required Query Params:** None

### `POST` `/payment_dispute/{payment_dispute_id}/contest`
- **operationId:** `contestPaymentDispute`
- **Summary:** Contest Payment Dispute
- **Required Path Params:** `payment_dispute_id`
- **Required Query Params:** None

### `GET` `/payment_dispute/{payment_dispute_id}/fetch_evidence_content`
- **operationId:** `fetchEvidenceContent`
- **Summary:** Get Payment Dispute Evidence File
- **Required Path Params:** `payment_dispute_id`
- **Required Query Params:** `evidence_id`, `file_id`

### `POST` `/payment_dispute/{payment_dispute_id}/update_evidence`
- **operationId:** `updateEvidence`
- **Summary:** Update evidence
- **Required Path Params:** `payment_dispute_id`
- **Required Query Params:** None

### `POST` `/payment_dispute/{payment_dispute_id}/upload_evidence_file`
- **operationId:** `uploadEvidenceFile`
- **Summary:** Upload an Evidence File
- **Required Path Params:** `payment_dispute_id`
- **Required Query Params:** None

### `GET` `/payment_dispute_summary`
- **operationId:** `getPaymentDisputeSummaries`
- **Summary:** Search Payment Dispute by Filters
- **Required Path Params:** None
- **Required Query Params:** None

*Total endpoints in Fulfillment API: 15*

---

# Account v1 API (vv1.9.3)

**Base URL:** `https://api.ebay.com{basePath}`

### `GET` `/advertising_eligibility`
- **operationId:** `getAdvertisingEligibility`
- **Summary:** This method allows developers to check the seller eligibility status for eBay advertising programs.
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/bulk_create_or_replace_sales_tax`
- **operationId:** `bulkCreateOrReplaceSalesTax`
- **Summary:** This method creates or updates multiple sales-tax table entries.<br><br><i>Sales-tax tables</i> can be set up for countries that support different ...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/custom_policy/`
- **operationId:** `getCustomPolicies`
- **Summary:** This method retrieves the list of custom policies defined for a seller's account. To limit the returned custom policies, specify the <b>policy_type...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/custom_policy/`
- **operationId:** `createCustomPolicy`
- **Summary:** This method creates a new custom policy that specifies the seller's terms for complying with local governmental regulations. Each Custom Policy tar...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/custom_policy/{custom_policy_id}`
- **operationId:** `getCustomPolicy`
- **Summary:** This method retrieves the custom policy specified by the <b>custom_policy_id</b> path parameter.
- **Required Path Params:** `custom_policy_id`
- **Required Query Params:** None

### `PUT` `/custom_policy/{custom_policy_id}`
- **operationId:** `updateCustomPolicy`
- **Summary:** This method updates an existing custom policy specified by the <b>custom_policy_id</b> path parameter. Since this method overwrites the policy's <b...
- **Required Path Params:** `custom_policy_id`
- **Required Query Params:** None

### `GET` `/fulfillment_policy`
- **operationId:** `getFulfillmentPolicies`
- **Summary:** This method retrieves all the fulfillment policies configured for the marketplace you specify using the <code>marketplace_id</code> query parameter.
- **Required Path Params:** None
- **Required Query Params:** `marketplace_id`

### `POST` `/fulfillment_policy/`
- **operationId:** `createFulfillmentPolicy`
- **Summary:** This method creates a new fulfillment policy for an eBay marketplace where the policy encapsulates seller's terms for fulfilling item purchases. Fu...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/fulfillment_policy/get_by_policy_name`
- **operationId:** `getFulfillmentPolicyByName`
- **Summary:** This method retrieves the details for a specific fulfillment policy. In the request, supply both the policy <code>name</code> and its associated <c...
- **Required Path Params:** None
- **Required Query Params:** `marketplace_id`, `name`

### `GET` `/fulfillment_policy/{fulfillmentPolicyId}`
- **operationId:** `getFulfillmentPolicy`
- **Summary:** This method retrieves the complete details of a fulfillment policy. Supply the ID of the policy you want to retrieve using the <b>fulfillmentPolicy...
- **Required Path Params:** `fulfillmentPolicyId`
- **Required Query Params:** None

### `PUT` `/fulfillment_policy/{fulfillmentPolicyId}`
- **operationId:** `updateFulfillmentPolicy`
- **Summary:** This method updates an existing fulfillment policy. Specify the policy you want to update using the <b>fulfillment_policy_id</b> path parameter. Su...
- **Required Path Params:** `fulfillmentPolicyId`
- **Required Query Params:** None

### `DELETE` `/fulfillment_policy/{fulfillmentPolicyId}`
- **operationId:** `deleteFulfillmentPolicy`
- **Summary:** This method deletes a fulfillment policy. Supply the ID of the policy you want to delete in the <b>fulfillmentPolicyId</b> path parameter.
- **Required Path Params:** `fulfillmentPolicyId`
- **Required Query Params:** None

### `GET` `/kyc`
- **operationId:** `getKYC`
- **Summary:** <span class="tablenote"><b>Note:</b> This method was originally created to see which onboarding requirements were still pending for sellers being o...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/payment_policy`
- **operationId:** `getPaymentPolicies`
- **Summary:** This method retrieves all the payment business policies configured for the marketplace you specify using the <code>marketplace_id</code> query para...
- **Required Path Params:** None
- **Required Query Params:** `marketplace_id`

### `POST` `/payment_policy`
- **operationId:** `createPaymentPolicy`
- **Summary:** This method creates a new payment policy where the policy encapsulates seller's terms for order payments. <br><br>A successful request returns the ...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/payment_policy/get_by_policy_name`
- **operationId:** `getPaymentPolicyByName`
- **Summary:** This method retrieves the details of a specific payment policy. Supply both the policy <code>name</code> and its associated <code>marketplace_id</c...
- **Required Path Params:** None
- **Required Query Params:** `marketplace_id`, `name`

### `GET` `/payment_policy/{payment_policy_id}`
- **operationId:** `getPaymentPolicy`
- **Summary:** This method retrieves the complete details of a payment policy. Supply the ID of the policy you want to retrieve using the <b>paymentPolicyId</b> p...
- **Required Path Params:** `payment_policy_id`
- **Required Query Params:** None

### `PUT` `/payment_policy/{payment_policy_id}`
- **operationId:** `updatePaymentPolicy`
- **Summary:** This method updates an existing payment policy. Specify the policy you want to update using the <b>payment_policy_id</b> path parameter. Supply a c...
- **Required Path Params:** `payment_policy_id`
- **Required Query Params:** None

### `DELETE` `/payment_policy/{payment_policy_id}`
- **operationId:** `deletePaymentPolicy`
- **Summary:** This method deletes a payment policy. Supply the ID of the policy you want to delete in the <b>paymentPolicyId</b> path parameter. 
- **Required Path Params:** `payment_policy_id`
- **Required Query Params:** None

### `GET` `/payments_program/{marketplace_id}/{payments_program_type}`
- **operationId:** `getPaymentsProgram`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is no longer applicable, as all seller accounts globally have been enabled for the new eBay paymen...
- **Required Path Params:** `marketplace_id`, `payments_program_type`
- **Required Query Params:** None

### `GET` `/payments_program/{marketplace_id}/{payments_program_type}/onboarding`
- **operationId:** `getPaymentsProgramOnboarding`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is no longer applicable, as all seller accounts globally have been enabled for the new eBay paymen...
- **Required Path Params:** `marketplace_id`, `payments_program_type`
- **Required Query Params:** None

### `GET` `/privilege`
- **operationId:** `getPrivileges`
- **Summary:** This method retrieves the seller's current set of privileges, including whether or not the seller's eBay registration has been completed, as well a...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/program/get_opted_in_programs`
- **operationId:** `getOptedInPrograms`
- **Summary:** This method gets a list of the seller programs that the seller has opted-in to.
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/program/opt_in`
- **operationId:** `optInToProgram`
- **Summary:** This method opts the seller in to an eBay seller program. Refer to the <a href="/api-docs/sell/account/overview.html#opt-in" target="_blank">Accoun...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/program/opt_out`
- **operationId:** `optOutOfProgram`
- **Summary:** This method opts the seller out of a seller program in which they are currently opted in to. A seller can retrieve a list of the seller programs th...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/rate_table`
- **operationId:** `getRateTables`
- **Summary:** This method retrieves a seller's <i>shipping rate tables</i> for the country specified in the <b>country_code</b> query parameter. If you call this...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/return_policy`
- **operationId:** `getReturnPolicies`
- **Summary:** This method retrieves all the return policies configured for the marketplace you specify using the <code>marketplace_id</code> query parameter.
- **Required Path Params:** None
- **Required Query Params:** `marketplace_id`

### `POST` `/return_policy`
- **operationId:** `createReturnPolicy`
- **Summary:** This method creates a new return policy where the policy encapsulates seller's terms for returning items.  <br><br>Each policy targets a specific m...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/return_policy/get_by_policy_name`
- **operationId:** `getReturnPolicyByName`
- **Summary:** This method retrieves the details of a specific return policy. Supply both the policy <code>name</code> and its associated <code>marketplace_id</co...
- **Required Path Params:** None
- **Required Query Params:** `marketplace_id`, `name`

### `GET` `/return_policy/{return_policy_id}`
- **operationId:** `getReturnPolicy`
- **Summary:** This method retrieves the complete details of the return policy specified by the <b>returnPolicyId</b> path parameter.
- **Required Path Params:** `return_policy_id`
- **Required Query Params:** None

### `PUT` `/return_policy/{return_policy_id}`
- **operationId:** `updateReturnPolicy`
- **Summary:** This method updates an existing return policy. Specify the policy you want to update using the <b>return_policy_id</b> path parameter. Supply a com...
- **Required Path Params:** `return_policy_id`
- **Required Query Params:** None

### `DELETE` `/return_policy/{return_policy_id}`
- **operationId:** `deleteReturnPolicy`
- **Summary:** This method deletes a return policy. Supply the ID of the policy you want to delete in the <b>returnPolicyId</b> path parameter.
- **Required Path Params:** `return_policy_id`
- **Required Query Params:** None

### `GET` `/sales_tax`
- **operationId:** `getSalesTaxes`
- **Summary:** Use this call to retrieve all sales tax table entries that the seller has defined for a specific country. All four response fields will be returned...
- **Required Path Params:** None
- **Required Query Params:** `country_code`

### `GET` `/sales_tax/{countryCode}/{jurisdictionId}`
- **operationId:** `getSalesTax`
- **Summary:** This call retrieves the current sales-tax table entry for a specific tax jurisdiction. Specify the jurisdiction to retrieve using the <b>countryCod...
- **Required Path Params:** `countryCode`, `jurisdictionId`
- **Required Query Params:** None

### `PUT` `/sales_tax/{countryCode}/{jurisdictionId}`
- **operationId:** `createOrReplaceSalesTax`
- **Summary:** This method creates or updates a sales-tax table entry for a jurisdiction. Specify the tax table entry you want to configure using the two path par...
- **Required Path Params:** `countryCode`, `jurisdictionId`
- **Required Query Params:** None

### `DELETE` `/sales_tax/{countryCode}/{jurisdictionId}`
- **operationId:** `deleteSalesTax`
- **Summary:** This call deletes a sales-tax table entry for a jurisdiction. Specify the jurisdiction to delete using the <b>countryCode</b> and <b>jurisdictionId...
- **Required Path Params:** `countryCode`, `jurisdictionId`
- **Required Query Params:** None

### `GET` `/subscription`
- **operationId:** `getSubscription`
- **Summary:** This method retrieves a list of subscriptions associated with the seller account.
- **Required Path Params:** None
- **Required Query Params:** None

*Total endpoints in Account v1 API: 37*

---

# Finances API (vv1.18.0)

**Base URL:** `https://apiz.ebay.com{basePath}`

### `GET` `/billing_activity`
- **operationId:** `getBillingActivities`
- **Summary:** <div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcF...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/payout`
- **operationId:** `getPayouts`
- **Summary:** <div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcF...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/payout/{payout_Id}`
- **operationId:** `getPayout`
- **Summary:** <div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcF...
- **Required Path Params:** `payout_Id`
- **Required Query Params:** None

### `GET` `/payout_summary`
- **operationId:** `getPayoutSummary`
- **Summary:** <div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcF...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/seller_funds_summary`
- **operationId:** `getSellerFundsSummary`
- **Summary:** <div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcF...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/transaction`
- **operationId:** `getTransactions`
- **Summary:** <div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcF...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/transaction_summary`
- **operationId:** `getTransactionSummary`
- **Summary:** <div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcF...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/transfer/{transfer_Id}`
- **operationId:** `getTransfer`
- **Summary:** <div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcF...
- **Required Path Params:** `transfer_Id`
- **Required Query Params:** None

*Total endpoints in Finances API: 8*

---

# Marketing API (vv1.22.2)

**Base URL:** `https://api.ebay.com{basePath}`

### `GET` `/ad_campaign`
- **operationId:** `getCampaigns`
- **Summary:** This method retrieves the details for all of the seller's defined campaigns. Request parameters can be used to retrieve a specific campaign, such a...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/ad_campaign`
- **operationId:** `createCampaign`
- **Summary:** This method can be used to create a Promoted Listings general, priority, or offsite campaign.<br><br>A Promoted Listings <i>campaign</i> is the str...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/ad_campaign/find_campaign_by_ad_reference`
- **operationId:** `findCampaignByAdReference`
- **Summary:** This method retrieves the campaigns containing the listing that is specified using either a listing ID, or an inventory reference ID and inventory ...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/ad_campaign/get_campaign_by_name`
- **operationId:** `getCampaignByName`
- **Summary:** This method retrieves the details of a single campaign, as specified with the <b>campaign_name</b> query parameter. Note that the campaign name you...
- **Required Path Params:** None
- **Required Query Params:** `campaign_name`

### `POST` `/ad_campaign/setup_quick_campaign`
- **operationId:** `setupQuickCampaign`
- **Summary:** This method allows the seller to expedite the creation of a priority strategy campaign.<br><br>Sellers only need to provide basic campaign informat...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/ad_campaign/suggest_budget`
- **operationId:** `suggestBudget`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only supported for Promoted Offsite campaigns. Sellers can use the <a href="/api-docs/sell/acco...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/ad_campaign/suggest_max_cpc`
- **operationId:** `suggestMaxCpc`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only supported for smart targeting priority strategy campaigns. Sellers can use the <a href="/a...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/ad_campaign/{campaign_id}`
- **operationId:** `getCampaign`
- **Summary:** This method retrieves the details of a single campaign, as specified with the <b>campaign_id</b> query parameter.  <p>This method returns all the d...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `DELETE` `/ad_campaign/{campaign_id}`
- **operationId:** `deleteCampaign`
- **Summary:** This method deletes the campaign specified by the <code>campaign_id</code> query parameter.<br /><br /><span class="tablenote"><b>Note: </b> You ca...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `GET` `/ad_campaign/{campaign_id}/ad`
- **operationId:** `getAds`
- **Summary:** This method retrieves Promoted Listings ads that are associated with listings created with either the <a href="/Devzone/XML/docs/Reference/eBay/ind...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/ad`
- **operationId:** `createAdByListingId`
- **Summary:** This method adds a listing to an existing Promoted Listings campaign using a <b>listingId</b> value generated by the <a href="/Devzone/XML/docs/Ref...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `GET` `/ad_campaign/{campaign_id}/ad/{ad_id}`
- **operationId:** `getAd`
- **Summary:** This method retrieves the specified ad from the specified campaign.  <p>In the request, supply the <b>campaign_id</b> and <b>ad_id</b> as path para...
- **Required Path Params:** `ad_id`, `campaign_id`
- **Required Query Params:** None

### `DELETE` `/ad_campaign/{campaign_id}/ad/{ad_id}`
- **operationId:** `deleteAd`
- **Summary:** This method removes the specified ad from the specified campaign.<br /><br />Pass the ID of the ad to delete with the ID of the campaign associated...
- **Required Path Params:** `ad_id`, `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/ad/{ad_id}/update_bid`
- **operationId:** `updateBid`
- **Summary:** This method updates the bid percentage (also known as the "ad rate") for the specified ad in the specified campaign. <p>In the request, supply the ...
- **Required Path Params:** `ad_id`, `campaign_id`
- **Required Query Params:** None

### `GET` `/ad_campaign/{campaign_id}/ad_group`
- **operationId:** `getAdGroups`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/ad_group`
- **operationId:** `createAdGroup`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `GET` `/ad_campaign/{campaign_id}/ad_group/{ad_group_id}`
- **operationId:** `getAdGroup`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `ad_group_id`, `campaign_id`
- **Required Query Params:** None

### `PUT` `/ad_campaign/{campaign_id}/ad_group/{ad_group_id}`
- **operationId:** `updateAdGroup`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `ad_group_id`, `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_bids`
- **operationId:** `suggestBids`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `ad_group_id`, `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/ad_group/{ad_group_id}/suggest_keywords`
- **operationId:** `suggestKeywords`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `ad_group_id`, `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/bulk_create_ads_by_inventory_reference`
- **operationId:** `bulkCreateAdsByInventoryReference`
- **Summary:** This method adds multiple listings that are managed with the <a href="/api-docs/sell/inventory/resources/methods" title="Inventory API Reference">I...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/bulk_create_ads_by_listing_id`
- **operationId:** `bulkCreateAdsByListingId`
- **Summary:** This method adds multiple listings to an existing Promoted Listings campaign using <b>listingId</b> values generated by the <a href="/Devzone/XML/d...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/bulk_create_keyword`
- **operationId:** `bulkCreateKeyword`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/bulk_delete_ads_by_inventory_reference`
- **operationId:** `bulkDeleteAdsByInventoryReference`
- **Summary:** This method works with listings created with the <a href="/api-docs/sell/inventory/resources/methods" title="Inventory API Reference">Inventory API...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/bulk_delete_ads_by_listing_id`
- **operationId:** `bulkDeleteAdsByListingId`
- **Summary:** This method works with listing IDs created with either the <a href="/Devzone/XML/docs/Reference/eBay/index.html" title="Trading API Reference">Trad...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_inventory_reference`
- **operationId:** `bulkUpdateAdsBidByInventoryReference`
- **Summary:** This method works with listings created with either the <a href="/Devzone/XML/docs/Reference/eBay/index.html" title="Trading API Reference">Trading...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/bulk_update_ads_bid_by_listing_id`
- **operationId:** `bulkUpdateAdsBidByListingId`
- **Summary:** This method works with listings created with either the <a href="/Devzone/XML/docs/Reference/eBay/index.html" title="Trading API Reference">Trading...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/bulk_update_ads_status`
- **operationId:** `bulkUpdateAdsStatus`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the priority strategy program. Fo...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/bulk_update_ads_status_by_listing_id`
- **operationId:** `bulkUpdateAdsStatusByListingId`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/bulk_update_keyword`
- **operationId:** `bulkUpdateKeyword`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/clone`
- **operationId:** `cloneCampaign`
- **Summary:** This method clones (makes a copy of) the specified campaign's <b>campaign criterion</b>. The <b>campaign criterion</b> is a container for the field...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/create_ads_by_inventory_reference`
- **operationId:** `createAdsByInventoryReference`
- **Summary:** This method adds a listing that is managed with the <a href="/api-docs/sell/inventory/resources/methods" title="Inventory API Reference">Inventory ...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/delete_ads_by_inventory_reference`
- **operationId:** `deleteAdsByInventoryReference`
- **Summary:** This method works with listings that are managed with the <a href="/api-docs/sell/inventory/resources/methods" title="Inventory API Reference">Inve...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/end`
- **operationId:** `endCampaign`
- **Summary:** This method ends an active (<code>RUNNING</code>) or paused campaign. Specify the campaign you want to end by supplying its campaign ID in a query ...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `GET` `/ad_campaign/{campaign_id}/get_ads_by_inventory_reference`
- **operationId:** `getAdsByInventoryReference`
- **Summary:** This method retrieves Promoted Listings ads associated with listings that are managed with the <a href="/api-docs/sell/inventory/resources/methods"...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** `inventory_reference_id`, `inventory_reference_type`

### `GET` `/ad_campaign/{campaign_id}/keyword`
- **operationId:** `getKeywords`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/keyword`
- **operationId:** `createKeyword`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `GET` `/ad_campaign/{campaign_id}/keyword/{keyword_id}`
- **operationId:** `getKeyword`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`, `keyword_id`
- **Required Query Params:** None

### `PUT` `/ad_campaign/{campaign_id}/keyword/{keyword_id}`
- **operationId:** `updateKeyword`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`, `keyword_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/launch`
- **operationId:** `launchCampaign`
- **Summary:** This method launches a priority strategy campaign created using the <a href="/api-docs/sell/marketing/resources/campaign/methods/setupQuickCampaign...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/pause`
- **operationId:** `pauseCampaign`
- **Summary:** This method pauses an active (RUNNING) campaign.  <p>You can restart the campaign by calling <a href="/api-docs/sell/marketing/resources/campaign/m...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/resume`
- **operationId:** `resumeCampaign`
- **Summary:** This method resumes a paused campaign, as long as its end date is in the future. Supply the <b>campaign_id</b> for the campaign you want to restart...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `GET` `/ad_campaign/{campaign_id}/suggest_items`
- **operationId:** `suggestItems`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/update_ad_rate_strategy`
- **operationId:** `updateAdRateStrategy`
- **Summary:** This method updates the ad rate strategy for an existing rules-based general strategy ad campaign that uses the Cost Per Sale (CPS) funding model.<...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/update_bidding_strategy`
- **operationId:** `updateBiddingStrategy`
- **Summary:** This method allows sellers to change the bidding strategy for a specified Cost Per Click (CPC) campaign that uses manual targeting. Available biddi...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/update_campaign_budget`
- **operationId:** `updateCampaignBudget`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `POST` `/ad_campaign/{campaign_id}/update_campaign_identification`
- **operationId:** `updateCampaignIdentification`
- **Summary:** This method can be used to change the name of a campaign, as well as modify the start or end dates. <p>Specify the <b>campaign_id</b> you want to u...
- **Required Path Params:** `campaign_id`
- **Required Query Params:** None

### `GET` `/ad_report/{report_id}`
- **operationId:** `getReport`
- **Summary:** This call downloads the report as specified by the <b>report_id</b> path parameter.  <br><br>Call <a href="/api-docs/sell/marketing/resources/ad_re...
- **Required Path Params:** `report_id`
- **Required Query Params:** None

### `GET` `/ad_report_metadata`
- **operationId:** `getReportMetadata`
- **Summary:** This call retrieves information that details the fields used in each of the Promoted Listings reports. Use the returned information to configure th...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/ad_report_metadata/{report_type}`
- **operationId:** `getReportMetadataForReportType`
- **Summary:** This call retrieves metadata that details the fields used by a specific Promoted Listings report type. Use the <b>report_type</b> path parameter to...
- **Required Path Params:** `report_type`
- **Required Query Params:** None

### `GET` `/ad_report_task`
- **operationId:** `getReportTasks`
- **Summary:** This method returns information on all the existing report tasks related to a seller. <p>Use the <b>report_task_statuses</b> query parameter to con...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/ad_report_task`
- **operationId:** `createReportTask`
- **Summary:** This method creates a <i>report task</i>, which generates a Promoted Listings report based on the values specified in the call.<br /><br />The repo...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/ad_report_task/{report_task_id}`
- **operationId:** `getReportTask`
- **Summary:** This call returns the details of a specific Promoted Listings report task, as specified by the <b>report_task_id</b> path parameter. <p>The report ...
- **Required Path Params:** `report_task_id`
- **Required Query Params:** None

### `DELETE` `/ad_report_task/{report_task_id}`
- **operationId:** `deleteReportTask`
- **Summary:** This call deletes the report task specified by the <b>report_task_id</b> path parameter. This method also deletes any reports generated by the repo...
- **Required Path Params:** `report_task_id`
- **Required Query Params:** None

### `POST` `/bulk_create_negative_keyword`
- **operationId:** `bulkCreateNegativeKeyword`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/bulk_update_negative_keyword`
- **operationId:** `bulkUpdateNegativeKeyword`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/email_campaign`
- **operationId:** `getEmailCampaigns`
- **Summary:** This method retrieves a list of email campaigns from a seller's eBay store.<br><br>Users can filter the results by <a href="/api-docs/sell/marketin...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/email_campaign`
- **operationId:** `createEmailCampaign`
- **Summary:** This method creates a new email campaign. An eBay store owner can create six different types of email campaigns: Welcome, New products & collection...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/email_campaign/audience`
- **operationId:** `getAudiences`
- **Summary:** This method retrieves all available email newsletter audiences for the <a href="/api-docs/sell/marketing/types/api:CampaignTypeEnum">email campaign...
- **Required Path Params:** None
- **Required Query Params:** `emailCampaignType`

### `GET` `/email_campaign/report`
- **operationId:** `getEmailReport`
- **Summary:** This method returns the seller's email campaign performance report for a time period specified by the <b>startDate</b> and <b>endDate</b> path para...
- **Required Path Params:** None
- **Required Query Params:** `endDate`, `startDate`

### `GET` `/email_campaign/{email_campaign_id}`
- **operationId:** `getEmailCampaign`
- **Summary:** This method returns the details of a single email campaign specified by the <b>email_campaign_id</b> path parameter.<br><br>Call <a href="/api-docs...
- **Required Path Params:** `email_campaign_id`
- **Required Query Params:** None

### `PUT` `/email_campaign/{email_campaign_id}`
- **operationId:** `updateEmailCampaign`
- **Summary:** This method lets users update an existing email campaign. Pass the <b>emailCampaignId</b> in the request URL and specify the changes to field value...
- **Required Path Params:** `email_campaign_id`
- **Required Query Params:** None

### `DELETE` `/email_campaign/{email_campaign_id}`
- **operationId:** `deleteEmailCampaign`
- **Summary:** This method deletes the email campaign specified by the <b>email_campaign_id</b> path parameter.<br><br>Call <a href="/api-docs/sell/marketing/reso...
- **Required Path Params:** `email_campaign_id`
- **Required Query Params:** None

### `GET` `/email_campaign/{email_campaign_id}/email_preview`
- **operationId:** `getEmailPreview`
- **Summary:** This method returns a preview of the email sent by the email campaign indicated by the <b>email_campaign_id</b> path parameter.<br><br>Call <a href...
- **Required Path Params:** `email_campaign_id`
- **Required Query Params:** None

### `POST` `/item_price_markdown`
- **operationId:** `createItemPriceMarkdownPromotion`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/item_price_markdown/{promotion_id}`
- **operationId:** `getItemPriceMarkdownPromotion`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** `promotion_id`
- **Required Query Params:** None

### `PUT` `/item_price_markdown/{promotion_id}`
- **operationId:** `updateItemPriceMarkdownPromotion`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** `promotion_id`
- **Required Query Params:** None

### `DELETE` `/item_price_markdown/{promotion_id}`
- **operationId:** `deleteItemPriceMarkdownPromotion`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** `promotion_id`
- **Required Query Params:** None

### `POST` `/item_promotion`
- **operationId:** `createItemPromotion`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/item_promotion/{promotion_id}`
- **operationId:** `getItemPromotion`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** `promotion_id`
- **Required Query Params:** None

### `PUT` `/item_promotion/{promotion_id}`
- **operationId:** `updateItemPromotion`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** `promotion_id`
- **Required Query Params:** None

### `DELETE` `/item_promotion/{promotion_id}`
- **operationId:** `deleteItemPromotion`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** `promotion_id`
- **Required Query Params:** None

### `GET` `/negative_keyword`
- **operationId:** `getNegativeKeywords`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/negative_keyword`
- **operationId:** `createNegativeKeyword`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/negative_keyword/{negative_keyword_id}`
- **operationId:** `getNegativeKeyword`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the priority strategy program. Fo...
- **Required Path Params:** `negative_keyword_id`
- **Required Query Params:** None

### `PUT` `/negative_keyword/{negative_keyword_id}`
- **operationId:** `updateNegativeKeyword`
- **Summary:** <span class="tablenote"><b>Note:</b> This method is only available for select partners who have been approved for the eBay priority strategy progra...
- **Required Path Params:** `negative_keyword_id`
- **Required Query Params:** None

### `GET` `/promotion`
- **operationId:** `getPromotions`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** None
- **Required Query Params:** `marketplace_id`

### `GET` `/promotion/{promotion_id}/get_listing_set`
- **operationId:** `getListingSet`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** `promotion_id`
- **Required Query Params:** None

### `POST` `/promotion/{promotion_id}/pause`
- **operationId:** `pausePromotion`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** `promotion_id`
- **Required Query Params:** None

### `POST` `/promotion/{promotion_id}/resume`
- **operationId:** `resumePromotion`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** `promotion_id`
- **Required Query Params:** None

### `GET` `/promotion_report`
- **operationId:** `getPromotionReports`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** None
- **Required Query Params:** `marketplace_id`

### `GET` `/promotion_summary_report`
- **operationId:** `getPromotionSummaryReport`
- **Summary:** <span class="tablenote"><b>Note:</b> As of July 8th 2024, <i>promotions</i> are now being referred to as <i>discounts</i> on Seller Hub and eBay he...
- **Required Path Params:** None
- **Required Query Params:** `marketplace_id`

*Total endpoints in Marketing API: 82*

---

# Feed API (vv1.3.1)

**Base URL:** `https://api.ebay.com{basePath}`

### `GET` `/customer_service_metric_task`
- **operationId:** `getCustomerServiceMetricTasks`
- **Summary:** Use this method to return an array of customer service metric tasks. You can limit the tasks returned by specifying a date range. </p> <p> <span cl...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/customer_service_metric_task`
- **operationId:** `createCustomerServiceMetricTask`
- **Summary:** <p>Use this method to create a customer service metrics download task with filter criteria for the customer service metrics report. When using this...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/customer_service_metric_task/{task_id}`
- **operationId:** `getCustomerServiceMetricTask`
- **Summary:** <p>Use this method to retrieve customer service metric task details for the specified task. The input is <strong>task_id</strong>.</p>
- **Required Path Params:** `task_id`
- **Required Query Params:** None

### `GET` `/inventory_task`
- **operationId:** `getInventoryTasks`
- **Summary:** This method searches for multiple tasks of a specific feed type, and includes date filters and pagination.
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/inventory_task`
- **operationId:** `createInventoryTask`
- **Summary:** This method creates an inventory-related download task for a specified feed type with optional filter criteria. When using this method, specify the...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/inventory_task/{task_id}`
- **operationId:** `getInventoryTask`
- **Summary:** This method retrieves the task details and status of the specified inventory-related task. The input is <strong>task_id</strong>.
- **Required Path Params:** `task_id`
- **Required Query Params:** None

### `GET` `/order_task`
- **operationId:** `getOrderTasks`
- **Summary:** This method returns the details and status for an array of order tasks based on a specified <strong>feed_type</strong> or <strong>schedule_id</stro...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/order_task`
- **operationId:** `createOrderTask`
- **Summary:** This method creates an order download task with filter criteria for the order report. When using this method, specify the <b> feedType</b>, <b> sch...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/order_task/{task_id}`
- **operationId:** `getOrderTask`
- **Summary:** This method retrieves the task details and status of the specified task. The input is <strong>task_id</strong>. <p>For details about how this metho...
- **Required Path Params:** `task_id`
- **Required Query Params:** None

### `GET` `/schedule`
- **operationId:** `getSchedules`
- **Summary:** This method retrieves an array containing the details and status of all schedules based on the specified <strong>feed_type</strong>. Use this metho...
- **Required Path Params:** None
- **Required Query Params:** `feed_type`

### `POST` `/schedule`
- **operationId:** `createSchedule`
- **Summary:** This method creates a schedule, which is a subscription to the specified schedule template. A schedule periodically generates a report for the <str...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/schedule/{schedule_id}`
- **operationId:** `getSchedule`
- **Summary:** This method retrieves schedule details and status of the specified schedule. Specify the schedule to retrieve using the <strong>schedule_id</strong...
- **Required Path Params:** `schedule_id`
- **Required Query Params:** None

### `PUT` `/schedule/{schedule_id}`
- **operationId:** `updateSchedule`
- **Summary:** This method updates an existing schedule. Specify the schedule to update using the <strong>schedule_id</strong> path parameter. If the schedule tem...
- **Required Path Params:** `schedule_id`
- **Required Query Params:** None

### `DELETE` `/schedule/{schedule_id}`
- **operationId:** `deleteSchedule`
- **Summary:** This method deletes an existing schedule. Specify the schedule to delete using the <strong>schedule_id</strong> path parameter.
- **Required Path Params:** `schedule_id`
- **Required Query Params:** None

### `GET` `/schedule/{schedule_id}/download_result_file`
- **operationId:** `getLatestResultFile`
- **Summary:** This method downloads the latest Order Report generated by the schedule. The response of this call is a compressed or uncompressed CSV, XML, or JSO...
- **Required Path Params:** `schedule_id`
- **Required Query Params:** None

### `GET` `/schedule_template`
- **operationId:** `getScheduleTemplates`
- **Summary:** This method retrieves an array containing the details and status of all schedule templates based on the specified <strong>feed_type</strong>. Use t...
- **Required Path Params:** None
- **Required Query Params:** `feed_type`

### `GET` `/schedule_template/{schedule_template_id}`
- **operationId:** `getScheduleTemplate`
- **Summary:** This method retrieves the details of the specified template. Specify the template to retrieve using the <strong>schedule_template_id</strong> path ...
- **Required Path Params:** `schedule_template_id`
- **Required Query Params:** None

### `GET` `/task`
- **operationId:** `getTasks`
- **Summary:** This method returns the details and status for an array of tasks based on a specified <strong>feed_type</strong> or <strong>schedule_id</strong>. S...
- **Required Path Params:** None
- **Required Query Params:** None

### `POST` `/task`
- **operationId:** `createTask`
- **Summary:** This method creates an upload task or a download task without filter criteria. When using this method, specify the <b> feedType</b> and the feed fi...
- **Required Path Params:** None
- **Required Query Params:** None

### `GET` `/task/{task_id}`
- **operationId:** `getTask`
- **Summary:** This method retrieves the details and status of the specified task. The input is <strong>task_id</strong>. <br /><br />For details of how this meth...
- **Required Path Params:** `task_id`
- **Required Query Params:** None

### `GET` `/task/{task_id}/download_input_file`
- **operationId:** `getInputFile`
- **Summary:** This method downloads the file previously uploaded using <strong>uploadFile</strong>. Specify the task_id from the <strong>uploadFile</strong> call...
- **Required Path Params:** `task_id`
- **Required Query Params:** None

### `GET` `/task/{task_id}/download_result_file`
- **operationId:** `getResultFile`
- **Summary:** This method retrieves the generated file that is associated with the specified task ID. The response of this call is a compressed or uncompressed C...
- **Required Path Params:** `task_id`
- **Required Query Params:** None

### `POST` `/task/{task_id}/upload_file`
- **operationId:** `uploadFile`
- **Summary:** This method associates the specified file with the specified task ID and uploads the input file. After the file has been uploaded, the processing o...
- **Required Path Params:** `task_id`
- **Required Query Params:** None

*Total endpoints in Feed API: 23*

---

# Taxonomy API (vv1.1.1)

**Base URL:** `https://api.ebay.com{basePath}`

### `GET` `/category_tree/{category_tree_id}`
- **operationId:** `getCategoryTree`
- **Summary:** Get a Category Tree
- **Required Path Params:** `category_tree_id`
- **Required Query Params:** None

### `GET` `/category_tree/{category_tree_id}/fetch_item_aspects`
- **operationId:** `fetchItemAspects`
- **Summary:** Get Aspects for All Leaf Categories in a Marketplace
- **Required Path Params:** `category_tree_id`
- **Required Query Params:** None

### `GET` `/category_tree/{category_tree_id}/get_category_subtree`
- **operationId:** `getCategorySubtree`
- **Summary:** Get a Category Subtree
- **Required Path Params:** `category_tree_id`
- **Required Query Params:** `category_id`

### `GET` `/category_tree/{category_tree_id}/get_category_suggestions`
- **operationId:** `getCategorySuggestions`
- **Summary:** Get Suggested Categories
- **Required Path Params:** `category_tree_id`
- **Required Query Params:** `q`

### `GET` `/category_tree/{category_tree_id}/get_compatibility_properties`
- **operationId:** `getCompatibilityProperties`
- **Summary:** Get Compatibility Properties
- **Required Path Params:** `category_tree_id`
- **Required Query Params:** `category_id`

### `GET` `/category_tree/{category_tree_id}/get_compatibility_property_values`
- **operationId:** `getCompatibilityPropertyValues`
- **Summary:** Get Compatibility Property Values
- **Required Path Params:** `category_tree_id`
- **Required Query Params:** `compatibility_property`, `category_id`

### `GET` `/category_tree/{category_tree_id}/get_expired_categories`
- **operationId:** `getExpiredCategories`
- **Summary:** This method retrieves the mappings of expired leaf categories in the specified category tree to their corresponding active leaf categories. Note th...
- **Required Path Params:** `category_tree_id`
- **Required Query Params:** None

### `GET` `/category_tree/{category_tree_id}/get_item_aspects_for_category`
- **operationId:** `getItemAspectsForCategory`
- **Summary:** This call returns a list of <i>aspects</i> that are appropriate or necessary for accurately describing items in the specified leaf category. Each a...
- **Required Path Params:** `category_tree_id`
- **Required Query Params:** `category_id`

### `GET` `/get_default_category_tree_id`
- **operationId:** `getDefaultCategoryTreeId`
- **Summary:** Get a Default Category Tree ID
- **Required Path Params:** None
- **Required Query Params:** `marketplace_id`

*Total endpoints in Taxonomy API: 9*

---

## Grand Total: 217 endpoints across all 8 APIs