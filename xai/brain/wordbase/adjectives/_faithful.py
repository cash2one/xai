

#calss header
class _FAITHFUL():
	def __init__(self,): 
		self.name = "FAITHFUL"
		self.definitions = [u'firm and not changing in your friendship with or support for a person or an organization, or in your belief in your principles: ', u'If your husband, wife, or partner is faithful, he or she does not have a sexual relationship with anyone else: ', u'to continue to support or follow something: ', u'true or not changing any of the details, facts, style, etc. of the original: ', u'following a particular religion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
