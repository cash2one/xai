

#calss header
class _POSSESSIVE():
	def __init__(self,): 
		self.name = "POSSESSIVE"
		self.definitions = [u'If you are possessive about something that you own, you do not like lending it to other people or sharing it with other people: ', u"Someone who is possessive in his or her feelings and behaviour towards or about another person wants to have all of that person's love and attention and will not share it with anyone else: ", u'In grammar, a possessive word, form, etc. shows who or what something belongs to: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
