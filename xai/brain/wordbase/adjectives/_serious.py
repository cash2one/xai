

#calss header
class _SERIOUS():
	def __init__(self,): 
		self.name = "SERIOUS"
		self.definitions = [u'severe in effect; bad: ', u'very ill', u'not joking or intended to be funny: ', u'A serious person is quiet, thinks carefully about things, and does not laugh a lot: ', u'determined to follow a particular plan of action: ', u'If two people who have a loving relationship are serious about each other, they intend to stay with each other for a long time and possibly marry: ', u'needing or deserving your complete attention: ', u'extreme in degree or amount: ', u'very good of its type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
