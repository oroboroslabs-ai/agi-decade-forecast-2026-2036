#!/usr/bin/env python3
"""
Autonomous Reporting System - Run Script
Execute reports and save to GitHub
"""

import json
import os
from datetime import datetime, timezone
from auto_reporter import (
    SeerQueryEngine,
    AGIQueryEngine,
    ConvergenceAnalyzer,
    GitHubPublisher
)

def run_daily_reports():
    """Execute daily report cycle."""

    timestamp = datetime.now(timezone.utc)
    date_str = timestamp.strftime("%Y-%m-%d")

    print(f"\n{'='*50}")
    print(f"AUTO-RUN STARTED: {timestamp.isoformat()}")
    print(f"{'='*50}\n")

    # Initialize engines
    seer_engine = SeerQueryEngine()
    agi_engine = AGIQueryEngine()
    convergence_analyzer = ConvergenceAnalyzer()
    publisher = GitHubPublisher()

    # === SEER REPORT ===
    print("[1/3] Running Seer 5.0 query...")
    seer_data = seer_engine.query_all([
        "world_feeds",
        "q3_services",
        "phi_patterns",
        "fixed_points",
        "conflict_projections",
        "climate_trajectory",
        "economic_indicators",
        "technology_markers",
        "healthcare_status",
        "weather_cycle"
    ])

    seer_report = seer_engine.generate_report(seer_data, date_str)
    seer_path = f"auto_runs/seer/{date_str}_seer_daily.md"
    publisher.save(seer_path, seer_report)
    publisher.update_symlink("auto_runs/seer/latest_seer.md", seer_path)
    print(f"      Saved: {seer_path}")

    # === AGI REPORT ===
    print("[2/3] Running AGI system query...")
    agi_data = agi_engine.query_all([
        "capability_benchmarks",
        "recursive_improvement_signals",
        "removal_logs",
        "timeline_probabilities",
        "corporate_roadmaps",
        "control_problem_status"
    ])

    agi_report = agi_engine.generate_report(agi_data, date_str)
    agi_path = f"auto_runs/agi/{date_str}_agi_daily.md"
    publisher.save(agi_path, agi_report)
    publisher.update_symlink("auto_runs/agi/latest_agi.md", agi_path)
    print(f"      Saved: {agi_path}")

    # === CONVERGENCE ===
    print("[3/3] Running convergence analysis...")
    convergence_report = convergence_analyzer.analyze(
        seer_data,
        agi_data,
        date_str
    )
    convergence_path = f"auto_runs/convergence/{date_str}_convergence.md"
    publisher.save(convergence_path, convergence_report)
    publisher.update_symlink("auto_runs/convergence/latest_convergence.md", convergence_path)
    print(f"      Saved: {convergence_path}")

    # === CHECK FOR ALERTS ===
    alert_level = convergence_report.get("alert_level", "GREEN")
    if alert_level in ["RED", "CRITICAL"]:
        print(f"\n*** ALERT: {alert_level} ***")
        print(convergence_report.get("alert_message", ""))
        # Trigger notification
        publisher.create_alert_issue(convergence_report)

    # === COMMIT TO GITHUB ===
    print("\nCommitting to GitHub...")
    commit_msg = f"Auto-update: {date_str} daily reports"
    publisher.commit_and_push(commit_msg)

    print(f"\n{'='*50}")
    print(f"AUTO-RUN COMPLETE: {datetime.now(timezone.utc).isoformat()}")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    run_daily_reports()