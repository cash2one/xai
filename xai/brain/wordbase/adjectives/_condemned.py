

#calss header
class _CONDEMNED():
	def __init__(self,): 
		self.name = "CONDEMNED"
		self.definitions = [u'A condemned person is someone who is going to be killed, especially as a punishment for having committed a very serious crime, such as murder.', u'A condemned building that has been officially judged not safe for people to live in or to use, or food that has been officially judged not safe to eat.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
