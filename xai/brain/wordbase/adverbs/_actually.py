

#calss header
class _ACTUALLY():
	def __init__(self,): 
		self.name = "ACTUALLY"
		self.definitions = [u'in fact or really: ', u'used in sentences in which there is information that is in some way surprising or the opposite of what most people would expect: ', u'used as a way of making a sentence slightly more polite, for example when you are expressing an opposing opinion, correcting what someone else has said, or refusing an offer: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
