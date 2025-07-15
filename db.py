
import sqlite3

def init_db():
    conn = sqlite3.connect("nexmax.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS campaigns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            campaignName TEXT,
            startDate TEXT,
            endDate TEXT,
            objective TEXT,
            description TEXT,
            campaignType TEXT,
            merchantLink TEXT,
            network TEXT,
            zipcode TEXT,
            location TEXT,
            languages TEXT,
            presetAdGroup TEXT,
            productGroup TEXT,
            keywordGroup TEXT,
            maxBudget REAL,
            optimizeTowards TEXT,
            targetROAS REAL,
            forecast TEXT,
            apis TEXT,
            realTimeDataFeeds TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_campaign(data):
    conn = sqlite3.connect("nexmax.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO campaigns (
            campaignName, startDate, endDate, objective, description, campaignType, merchantLink,
            network, zipcode, location, languages, presetAdGroup, productGroup, keywordGroup, maxBudget,
            optimizeTowards, targetROAS, forecast, apis, realTimeDataFeeds
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("campaignName"),
        data.get("startDate"),
        data.get("endDate"),
        data.get("objective"),
        data.get("description"),
        data.get("campaignType"),
        data.get("merchantLink"),
        data.get("network"),
        data.get("zipcode"),
        data.get("location"),
        data.get("languages"),
        data.get("presetAdGroup"),
        data.get("productGroup"),
        data.get("keywordGroup"),
        float(data.get("maxBudget", 0)),
        data.get("optimizeTowards"),
        float(data.get("targetROAS", 0)),
        data.get("forecast"),
        data.get("apis"),
        data.get("realTimeDataFeeds")
    ))
    conn.commit()
    conn.close()
