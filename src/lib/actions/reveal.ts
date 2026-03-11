export function reveal(node: HTMLElement, { delay = 0, duration = 800, threshold = 0.1 } = {}) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    node.style.visibility = 'visible';
                    node.classList.add('animate-fade-in-up');
                }, delay);
                observer.unobserve(node);
            }
        });
    }, { threshold });

    node.style.visibility = 'hidden';
    observer.observe(node);

    return {
        destroy() {
            observer.disconnect();
        }
    };
}
