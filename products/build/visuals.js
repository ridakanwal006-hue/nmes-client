// Adds illustrations and non-text visuals (diagrams, timelines, trackers, icon grids) to the USA/CA/UK editions.
module.exports = function addVisuals(products) {
  const DUMMY = { dummy: true, id: '', chapters: [] };
  const P = id => products.find(p => p.id === id + '-us-ca-uk') || DUMMY;
  const W = (p, ...a) => { if (!p.dummy) console.warn(...a); };
  const ch = (p, t) => p && p.chapters.find(c => c.title.toLowerCase().includes(t.toLowerCase()));
  const top = (p, t, ...bl) => { const c = ch(p, t); if (c) c.blocks.unshift(...bl); else W(p, 'no chapter', p.id, t); };
  const afterP = (p, t, ...bl) => { const c = ch(p, t); if (!c) return W(p, 'no chapter', p.id, t); const i = c.blocks.findIndex(b => b[0] === 'p'); c.blocks.splice(i + 1, 0, ...bl); };
  const bottom = (p, t, ...bl) => { const c = ch(p, t); if (c) c.blocks.push(...bl); else W(p, 'no chapter', p.id, t); };
  const repl = (p, t, type, ...bl) => { const c = ch(p, t); if (!c) return W(p, 'no chapter', p.id, t); const i = c.blocks.findIndex(b => b[0] === type); if (i < 0) return W(p, 'no block', t, type); c.blocks.splice(i, 1, ...bl); };
  const addChapter = (p, afterTitle, chapter) => { if (p.dummy) return; const i = p.chapters.findIndex(c => c.title.toLowerCase().includes(afterTitle.toLowerCase())); p.chapters.splice(i + 1, 0, chapter); };
  const tracker = (who) => ({ kicker: 'TRACKER', title: 'Your 30-day tracker', blocks: [
    ['p', 'Tick a box each day you do your small action. The highlighted days (7, 14, 21, 28) are your weekly reviews. A missed day is fine: carry on.'],
    ['cal', 30],
    ['art', 'calendar'],
    ['tip', 'How to use it', who === 'her' ? 'Print this page or keep it on your phone. Seeing the ticks build is encouraging.' : 'Print this page and put it where you will see it. Seeing the ticks build is encouraging.'],
  ] });

  // ---------- Conversation Starters After 35 ----------
  const cs = P('wolfe-conversation-starters-35-plus');
  cs.motif = 'bubbles';
  afterP(cs, 'Why talking feels harder', ['art', 'door', 'A new chapter, at your own pace']);
  (() => { const c = ch(cs, 'Eight things going on'); if (!c) return; const i = c.blocks.findIndex(b => b[0] === 'steps'); const rows = c.blocks[i][1];
    c.blocks[i] = ['steps', rows.slice(0, 4)];
    const idx = cs.chapters.indexOf(c);
    cs.chapters.splice(idx + 1, 0, { kicker: 'THE MIND', title: 'Eight things, continued', hideToc: true, blocks: [['steps', rows.slice(4)], ['art', 'umbrella', 'Fear shrinks when you say it out loud']] }); })();
  top(cs, 'Eight things going on', ['icons', [['walk', 'Rusty', 'out of practice'], ['eye', '"Foolish"', 'fear of a slip'], ['lock', 'Guarded', 'scared of being hurt'], ['users', 'Comparing', 'ex or late partner'], ['clock', 'No time', 'work, kids, care'], ['user', 'Too old?', 'age and body worry'], ['heart', 'Grief, guilt', 'after loss'], ['help', 'The rules?', 'apps and norms']], 4]);
  top(cs, 'Three findings', ['icons', [['help', 'Ask follow-ups', 'Huang et al., 2017'], ['eye', 'The liking gap', 'Boothby et al., 2018'], ['link', 'Match the depth', 'Aron et al., 1997']], 3]);
  top(cs, 'Five rules', ['flow', [['Ask', 'one question'], ['Follow up', 'before you switch'], ['Share', 'a little back'], ['Match', 'their depth'], ['Say', 'your pace']]]);
  bottom(cs, 'Five rules', ['dial', 'SLOWLY', 'QUICKLY', 0.28, 'Say where you are on this line out loud: **"I would like to go slowly."**']);
  repl(cs, 'Who goes first', 'steps', ['two', 'For him to ask her', ['Curious and light', 'Easy to answer', 'A clear offer to go at her pace', 'Warm, never pushy'], 'For her to ask him', ['What he is looking for', 'How he handles disagreement', 'What his life looks like', 'Checks intentions and pace early']], ['art', 'bubbles', 'Anyone can ask anything. Be kind.']);
  (() => { const c = ch(cs, 'What the answers tell you'); if (!c) return; const pIdx = c.blocks[0]; const tip = c.blocks.find(b => b[0] === 'tip');
    c.blocks = [pIdx, ['signals', [['go', 'They answer, then ask you something back.'], ['go', 'They are specific. A small story, not a slogan.'], ['go', 'They respect "no", "not yet" and "slower".'], ['go', 'You feel calmer after the chat, not more anxious.'], ['slow', 'They speak badly about every ex.'], ['slow', 'Their story changes between messages.'], ['stop', 'They push for contact or intimacy you do not want.'], ['stop', 'They ask for money, or for photos or details you are not ready to share.']]], tip]; })();
  repl(cs, 'A simple flow', 'steps', ['timeline', [['0-5 min', '**Say hello.** Ask about the journey and say one honest line: "I am a bit nervous."'], ['5-20 min', '**Easy questions.** Place, food, weekend. Follow up on one thing.'], ['20-45 min', '**Warm questions.** Work, family, interests. Share a little back.'], ['45-60 min', '**Check the pace.** "I enjoyed this. Would you like to do something again?" Yes, no and maybe are all fine.']]]);
  top(cs, 'Dating customs', ['art', 'coffee']);
  top(cs, 'If you think you are being scammed', ['art', 'shield']);
  top(cs, 'Small steps beat', ['art', 'path']);

  // ---------- Men: Starter ----------
  const st = P('wolfe-dating-again-starter-guide');
  st.motif = 'path';
  afterP(st, "You're not behind", ['art', 'door', 'Starting again, one small step at a time']);
  bottom(st, 'Grief, pace', ['dial', 'SLOWLY', 'QUICKLY', 0.28, 'There is no right speed. **Choose yours, and say it.**']);
  top(st, 'Where to meet people', ['icons', [['users', 'Friends', 'ask to be introduced'], ['walk', 'Activities', 'classes, clubs'], ['home', 'Community', 'faith, local events'], ['phone', 'Apps', 'with a safety routine']], 4]);
  top(st, 'Using dating apps safely', ['art', 'lock']);
  top(st, 'Photos and bio', ['art', 'photo']);
  top(st, 'Rejection and ghosting', ['art', 'umbrella']);
  top(st, 'Your 30-day starter plan', ['flow', [['Week 1', 'friends, story'], ['Week 2', 'photos, bio'], ['Week 3', 'first messages'], ['Week 4', 'a short coffee']]]);

  // ---------- Men: Profile Fixer ----------
  const pf = P('wolfe-profile-fixer-40-plus');
  pf.motif = 'photo';
  top(pf, 'What your profile is for', ['art', 'photo']);
  top(pf, 'Your photo plan', ['icons', [['camera', 'Headshot', 'clear smile'], ['walk', 'Doing something', 'a hobby'], ['users', 'With friends', 'easy to spot'], ['sun', 'Soft light', 'near a window']], 4]);
  top(pf, 'Safety on your profile', ['art', 'lock']);
  top(pf, '7-day profile tune-up', ['flow', [['Day 1', 'gather'], ['Day 2', 'pick six'], ['Day 3', 'write bio'], ['Day 4', 'prompts'], ['Day 5', 'safety'], ['Day 6', 'friend'], ['Day 7', 'publish']]]);

  // ---------- Men: 30-Day Challenge ----------
  const ch30 = P('wolfe-30-day-confidence-workbook');
  ch30.motif = 'stairs';
  addChapter(ch30, 'Where I am today', tracker('him'));
  top(ch30, 'My exposure ladder', ['ladder', ['Easiest: ________', '________', '________', '________', 'Hardest: ________']]);

  // ---------- Men: Rejection ----------
  const rj = P('wolfe-rejection-resilience-guide');
  rj.motif = 'umbrella';
  top(rj, 'What rejection is', ['art', 'umbrella', 'A no is weather, not a verdict']);
  top(rj, 'The first 24 hours', ['timeline', [['Hour 0-1', '**Breathe.** Do not reply. Put the phone down.'], ['Hour 1-6', '**Move.** A walk, a meal, a shower.'], ['Hour 6-24', '**Talk and sleep.** A friend, then rest.'], ['Day 2', '**One line** in your rejection log.']]]);

  // ---------- Scam checklist ----------
  const sc = P('wolfe-scam-red-flag-checklist');
  sc.motif = 'shield';
  top(sc, 'Where to report', ['art', 'shield']);

  // ---------- For her: Starter ----------
  const sh = P('wolfe-dating-again-starter-guide-for-her');
  sh.motif = 'door';
  afterP(sh, 'You are not behind', ['art', 'door', 'Starting again, at your pace']);
  bottom(sh, 'Grief, pace', ['dial', 'SLOWLY', 'QUICKLY', 0.28, 'There is no right speed. **Choose yours, and say it.**']);
  top(sh, 'Rebuild your circle', ['icons', [['users', 'Friends', 'make a plan'], ['walk', 'Activity', 'class or club'], ['phone', 'Your person', 'call before and after'], ['sun', 'Joy', 'one thing a week']], 4]);
  top(sh, 'Where to meet people', ['icons', [['users', 'Friends', 'ask to be introduced'], ['walk', 'Activities', 'classes, clubs'], ['home', 'Community', 'faith, local events'], ['phone', 'Apps', 'with safety routine']], 4]);
  top(sh, 'Using dating apps safely', ['art', 'lock']);
  top(sh, 'Photos and bio', ['art', 'photo']);
  top(sh, 'The first message', ['art', 'phone']);
  top(sh, 'first-date safety plan', ['art', 'pin']);
  (() => { const c = ch(sh, 'Is this relationship healthy'); if (!c) return; const tip = c.blocks.find(b => b[0] === 'tip');
    c.blocks = [['signals', [['go', 'You feel calmer, not more anxious, after you see them.'], ['go', 'They respect "no" and "not yet".'], ['go', 'They are honest, even when it is awkward.'], ['go', 'You keep your friends and your routines.'], ['slow', 'They tease or put you down, then say you are too sensitive.'], ['stop', 'They control who you see, what you wear or your money.'], ['stop', 'They check your phone or track your location.'], ['stop', 'They isolate you from friends and family, or you feel afraid of them.']]], tip]; })();
  top(sh, 'Your 30-day starter plan', ['flow', [['Week 1', 'friends, story'], ['Week 2', 'photos, bio'], ['Week 3', 'messages, video call'], ['Week 4', 'a safe coffee']]]);

  // ---------- For her: Profile ----------
  const ph = P('wolfe-profile-fixer-for-women-35-plus');
  ph.motif = 'photo';
  top(ph, 'What your profile is for', ['art', 'photo']);
  top(ph, 'Your photo plan', ['icons', [['camera', 'Headshot', 'clear smile'], ['walk', 'Doing something', 'a hobby'], ['users', 'With friends', 'easy to spot'], ['sun', 'Soft light', 'near a window']], 4]);
  top(ph, 'Safety on your profile', ['art', 'lock']);
  top(ph, '7-day profile tune-up', ['flow', [['Day 1', 'gather'], ['Day 2', 'pick six'], ['Day 3', 'write bio'], ['Day 4', 'prompts'], ['Day 5', 'safety'], ['Day 6', 'friend'], ['Day 7', 'publish']]]);

  // ---------- For her: 30-Day Challenge ----------
  const cw = P('wolfe-30-day-confidence-challenge-for-women');
  cw.motif = 'calendar';
  addChapter(cw, 'Where I am today', tracker('her'));
  top(cw, 'My exposure ladder', ['ladder', ['Easiest: ________', '________', '________', '________', 'Hardest: ________']]);
  top(cw, 'Changing a worrying thought', ['flow', [['The thought', 'what I tell myself'], ['For', 'what supports it'], ['Against', 'what else is true'], ['Kinder', 'a fairer version']]]);
};
