import sys
from git import Repo
from os import system, execle, environ
from git.exc import InvalidGitRepositoryError
from pyrogram.types import Message
from pyrogram import filters, Client
from GrootNetwork.config import UPSTREAM_REPO, UPSTREAM_BRANCH, OWNER_ID
from GrootNetwork.modules.helpers.filters import command


def gen_chlog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = ""
    tldr_log = ""
    ch = f"<b>updates for <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    ch_tl = f"updates for {ac_br}:"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n\nš¬ <b>{c.count()}</b> š <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"
            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> šØāš» <code>{c.author}</code>"
        )
        tldr_log += f"\n\nš¬ {c.count()} š [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] šØāš» {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("UPSTREAM_BRANCH", origin.refs.UPSTREAM_BRANCH)
        repo.heads.UPSTREAM_BRANCH.set_tracking_branch(origin.refs.UPSTREAM_BRANCH)
        repo.heads.UPSTREAM_BRANCH.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)


@Client.on_message(command(["update"]) & filters.user(OWNER_ID) & ~filters.edited)
async def update_bot(_, message: Message):
    chat_id = message.chat.id
    msg = await message.edit("**š„ į“Źį“į“į“ÉŖÉ“É¢ į“į“į“į“į“į“s āØ ...**")
    update_avail = updater()
    if update_avail:
        await msg.edit("**š„ Gį“É“ÉŖį“s Usį“ŹBį“į“ Uį“į“į“į“į“į“\nTį“ Lį“į“į“sį“ Vį“ŹsÉŖį“É“ š„ ...\n\nš Rį“sį“į“Źį“ÉŖÉ“É¢: Gį“É“ÉŖį“s Usį“Ź\nBį“į“, PŹį“į“sį“ Ā» Wį“ÉŖį“ āØ ...**")
        system("git pull -f && pip3 install -U -r Installer")
        system("python3 -m AdityaHalder")
        return
    await msg.edit(f"**š„ Gį“É“ÉŖį“s Usį“ŹBį“į“ AŹŹį“į“į“Ź\nUį“į“į“į“į“į“ Tį“ Lį“į“į“sį“ š„ ...\n\nš Fį“Ź AÉ“Ź Qį“į“ŹŹ āŗ Cį“É“į“į“į“į“\nTį“ Ā» @AdityaHalder āØ ...**")

__MODULE__ = "Uį“į“į“į“į“"
__HELP__ = f"""

**Nį“į“į“:**
**š„ TŹÉŖs PŹį“É¢ÉŖÉ“ Fį“Ź Uį“į“į“į“į“ Yį“į“Ź Usį“Ź Bį“į“**

**š®š³ Cį“į“į“į“É“į“ :**
`.update` - __Tį“ Uį“į“į“į“į“ Gį“É“ÉŖį“s Usį“ŹBį“į“ Tį“ Lį“į“į“sį“ Vį“ŹsÉŖį“É“ ...__
"""
