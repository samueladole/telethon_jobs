from app.domain.entities.resume import Resume

class ResumeRenderer:
    """Service to render Resume objects into text format."""

    def render_text(self, resume: Resume) -> str:
        """Renders a Resume object into a plain text representation."""
    
        lines = [resume.summary, "\nSkills:"]
        lines.extend(resume.skills)

        for exp in resume.experiences:
            lines.append(f"\n{exp.role} @ {exp.company}")
            for b in exp.bullets:
                lines.append(f"- {b}")

        return "\n".join(lines)
