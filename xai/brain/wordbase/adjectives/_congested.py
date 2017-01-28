

#calss header
class _CONGESTED():
	def __init__(self,): 
		self.name = "CONGESTED"
		self.definitions = [u'too blocked or crowded and causing difficulties', u'Congested roads and towns have too much traffic and movement is made difficult.', u'If you are or your nose is congested, you cannot breathe through your nose because it is blocked, usually during an infection.', u'Congested lungs or other body parts have become too full of blood or other liquid.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
