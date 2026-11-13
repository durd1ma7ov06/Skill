# Skill — ECC for Antigravity, Claude Code & Codex

ECC **v2.2.3** asosida tayyorlangan ko‘chma skill to‘plami. Istalgan loyihada tahlil, dizayn, backend, kod tekshiruvi va test ishlarida foydalanish uchun.

**Asl muallif:** [Affaan Mustafa va ECC hamjamiyati](https://github.com/affaan-m/ECC). **Litsenziya:** [MIT](LICENSE). Bu mustaqil qadoqlangan nusxa; rasmiy ECC repozitoriysi emas. Asl copyright yozuvlari saqlangan.

## Tarkibi

| Papka | Vazifasi |
|---|---|
| `Antigravity/` | Antigravity uchun moslashtirilgan skills, agents, rules va workflows |
| `Claude-Code/` | Claude Code uchun to‘liq ECC manbasi, native plugin va hook fayllari |
| `Codex/` | Native Codex plugin, ECC skillari va moslashtirilgan command skillari |
| `PROVENANCE.json` | Versiya, asl commit va haqiqiy tarkib sonlari |
| `SHA256SUMS.json` | Barcha tarqatiladigan fayllar tekshiruv summalari |

## Yuklab olish

```powershell
git clone https://github.com/durd1ma7ov06/Skill.git
cd Skill
python scripts/verify_bundle.py
```

Python 3.9+ faqat yaxlitlikni tekshirish uchun kerak. Klonlashdan keyin quyidagi yo‘llarning bittasini o‘zingiz ishlatadigan dastur uchun bajaring. Papkani nusxalashning o‘zi uchala dasturni avtomatik faollashtirmaydi.

## Claude Code

Claude Code ichida, klonlangan Skill papkasining to‘liq manzilini bering:

```text
/plugin marketplace add C:/Users/YOUR_NAME/Desktop/Skill
/plugin install ecc@skill-ecc
```

Claude Code native plugin qo‘llaydigan versiya talab qilinadi. Qo‘shimcha yo‘riqnoma: [upstream README](Claude-Code/README.md). Plugin hooklarini `settings.json` ichiga yana nusxalamang — ikki marta bajarilishi mumkin. `ecc@ecc` avval o‘rnatilgan bo‘lsa, ikkinchi nusxani parallel yoqmang.

## Codex

Terminalda klonlangan papkaning to‘liq manzilini kiriting:

```powershell
codex plugin marketplace add "$env:USERPROFILE\Desktop\Skill"
codex plugin add ecc@skill-ecc
codex plugin list --json
```

Codex native plugin qo‘llaydigan versiya kerak. Marketplace ildizi `Codex/` ichidagi to‘liq pluginni ko‘rsatadi. Ilovani qayta oching yoki yangi chat boshlang. Avvalgi `ecc@ecc` o‘rnatmasini parallel yoqish dublikatlar berishi mumkin. [Codex yo‘riqnomasi](Codex/.codex-plugin/README.md).

## Antigravity

Windows’da ushbu moslashtirma avval `%USERPROFILE%\.gemini\config` global ildizida ishlatilgan. Antigravity versiyangizning global customization manzilini tekshirib, `Antigravity/` ichidagi **skills**, **agents**, **rules**, **workflows** papkalarini o‘sha manzilga nusxalang. Mavjud fayllarni almashtirishdan oldin zaxiralang. Keyin ilovani qayta oching.

Fayllar nusxasi va yaxlitligi tekshirilgan; Antigravity ichidagi yangi suhbatda barcha workflowlarni bajarish sinovi qilinmagan. Adapter Claude Code hook/runtime imkoniyatlarining hammasini qo‘llamaydi. Claude/Codex hooklarini bu konfiguratsiyaga aralashtirmang.

## Ishlatish misollari

- “ECC yordamida loyihani tahlil qil, muammolarni tuzat va tekshir.”
- “Frontend dizaynini yaxshila; mavjud uslubni va mobil ko‘rinishni hisobga ol.”
- “Backend, autentifikatsiya va ruxsatlarni security-review bilan tekshir.”

Skill — agentga ish tartibini tushuntiradigan fayl. Agent ta’riflari avtomatik ravishda bir vaqtda ishga tushadigan xodimlar emas. Loyiha turi, host ruxsatlari va mavjud vositalar imkoniyatni belgilaydi. To‘plam obuna, model yoki API xizmatlarini bepul qilmaydi.

## Tekshiruv va xavfsizlik

```powershell
python scripts/verify_bundle.py
```

Tekshiruv yo‘llar papkadan tashqariga chiqmasligini, fayl hajmi va SHA-256 summalarini, native marketplace manzillarini tekshiradi. GitHub Actions xuddi shu tekshiruvni bajaradi; bundled hooklarni va installerlarni ishga tushirmaydi. SHA-256 ro‘yxati raqamli imzo emas.

Shaxsiy API kalitlari, auth fayllari, lokal bazalar, sayt audiolari va node_modules bu paketga qo‘shilmagan. O‘rnatilgan hook va MCP serverlari faqat hostning trust/ruxsat siyosati bilan ishlatiladi. Moslik farqlari va upstream hujjatlari har bir platforma papkasida saqlangan.

**Manba:** ECC v2.2.3, commit `c05b2d6614f62f6db0047669aa4eefb223d478f9`. Qadoqlash: 2026-11-13. [Tarkib va provenance](PROVENANCE.json).
